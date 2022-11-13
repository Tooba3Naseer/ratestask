from django.contrib import admin

from rates.models import Port, Region, Price

# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Customize admin portal for region model"""

    list_display = ("slug", "name", "parent_slug")
    search_fields = ("slug", "name")


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    """Customize admin portal for port model"""

    list_display = ("code", "name", "parent_slug")
    search_fields = ("code", "name")


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """Customize admin portal for price model"""

    list_display = ("orig_code", "dest_code", "day", "price")
    search_fields = ("day",)
