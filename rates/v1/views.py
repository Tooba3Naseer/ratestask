from django.db import connection

from rest_framework import status, views
from rest_framework.response import Response

from .serializers import ValidateQueryParamSerializer


class RatesView(views.APIView):
    """View for rates API"""

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"

        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row)) for row in cursor.fetchall()
        ]

    def get_ports(self, cursor, code):
        """
        This method will return the query that we will used as a subquery in the main query, written in the get method
        This method first get the port using its code, if it doesn't exist then it might be a region slug
        Next we will get all the ports located insdie that region.
        """

        query = f"""SELECT code FROM rates_port WHERE code = '{code}'"""
        cursor.execute(query)
        row = cursor.fetchone()
        if row and row[0] == code:
            return query

        sub_query = self.get_all_sub_regions_of_the_region(code)

        query = f"""
        SELECT code FROM rates_port WHERE parent_slug_id IN ({sub_query})
        """

        return query

    def get_all_sub_regions_of_the_region(self, region):
        """
        This method will return the query in which we are getting all the sub regions of the specified region
        """

        query = f"""
        WITH RECURSIVE generation AS (
            SELECT slug,
            name,
            parent_slug_id,
            0 AS generation_number
            FROM rates_region
            WHERE slug = '{region}'
        UNION ALL
            SELECT child.slug,
            child.name,
            child.parent_slug_id,
            generation_number+1 AS generation_number
            FROM rates_region child
            JOIN generation g
            ON g.slug = child.parent_slug_id
        )
        SELECT slug FROM generation
        UNION
        SELECT g.parent_slug_id AS slug FROM (SELECT * FROM generation WHERE generation_number != 0) AS g
        """

        return query

    def get_and_validate_query_params(self):
        """Get and validate query params"""

        query_params_dict = {
            "date_from": self.request.query_params.get("date_from"),
            "date_to": self.request.query_params.get("date_to"),
            "origin": self.request.query_params.get("origin"),
            "destination": self.request.query_params.get("destination")
        }
        ValidateQueryParamSerializer(
            data=query_params_dict).is_valid(raise_exception=True)

        return query_params_dict

    def get(self, request, *args, **kwargs):
        """HTTP Based GET API for rates"""

        query_params_dict = self.get_and_validate_query_params()

        with connection.cursor() as cursor:
            origins = self.get_ports(
                cursor, query_params_dict["origin"])
            destinations = self.get_ports(
                cursor, query_params_dict["destination"])

            date_from = query_params_dict["date_from"]
            date_to = query_params_dict["date_to"]

            query = f"""
            SELECT day,
            CASE 
            WHEN COUNT(*) < 3 THEN null 
            ELSE CAST(AVG(price) as int) 
            END AS average_price FROM rates_price
            WHERE orig_code_id IN ({origins}) AND dest_code_id IN ({destinations}) AND day BETWEEN '{date_from}' AND '{date_to}'
            GROUP BY day
            ORDER BY day ASC
            """
            cursor.execute(query)
            response = self.dictfetchall(cursor)

        return Response(response, status=status.HTTP_200_OK)
