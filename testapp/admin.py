from django.contrib import admin
from testapp.models import GlobexUsers

@admin.register(GlobexUsers)
class CitizensTypesAdmin(admin.ModelAdmin):
    list_display = ["name",]
