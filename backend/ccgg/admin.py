from django.contrib import admin

from .models import CO2_MM_MLO

class CO2_MM_MLOAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'average', 'interpolated')

admin.site.register(CO2_MM_MLO, CO2_MM_MLOAdmin)