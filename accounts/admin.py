from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Bill)
admin.site.register(Receipts)
admin.site.register(Report)

class AccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Account, AccountAdmin)