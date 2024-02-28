from django.contrib import admin

# Register your models here.
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "serialNumber", 
        "description",
        "supplier",
        "cost",
        "classed",
    )