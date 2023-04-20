from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Bill)
admin.site.register(Receipts)
admin.site.register(Account)
admin.site.register(Report)