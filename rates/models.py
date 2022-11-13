from django.db import models


class Region(models.Model):
    """Model class for region table"""

    slug = models.CharField(max_length=200, primary_key=True)
    name = models.TextField()
    parent_slug = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)


class Port(models.Model):
    """Model class for port table"""

    code = models.CharField(max_length=50, primary_key=True)
    name = models.TextField()
    parent_slug = models.ForeignKey(Region, on_delete=models.CASCADE)


class Price(models.Model):
    """Model class for price table"""

    orig_code = models.ForeignKey(
        Port, on_delete=models.CASCADE, related_name="orig_ports")
    dest_code = models.ForeignKey(
        Port, on_delete=models.CASCADE, related_name="dest_ports")
    day = models.DateField()
    price = models.PositiveIntegerField()
