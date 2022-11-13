from rest_framework import serializers


class ValidateQueryParamSerializer(serializers.Serializer):
    """
    Seiralizer for the validation of queryparams that we are taking from the rates API
    """

    date_from = serializers.DateField()
    date_to = serializers.DateField()
    origin = serializers.CharField()
    destination = serializers.CharField()

    def validate(self, data):
        if data["date_from"] > data["date_to"]:
            raise serializers.ValidationError(
                "Date from should be less than date to")

        return data
