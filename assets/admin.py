from django.contrib import admin
from .models import Asset, Manufacturer, Office, Organization
# Register your models here.
admin.site.register(Asset)
admin.site.register(Manufacturer)
admin.site.register(Office)
admin.site.register(Organization)