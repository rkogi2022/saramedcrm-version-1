from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

class BizLeadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(BizLead,BizLeadAdmin)

admin.site.register(Demo)