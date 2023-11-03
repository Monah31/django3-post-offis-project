from django.contrib import admin

from .models import Parcels, ParcelsCategory

admin.site.register(Parcels)
admin.site.register(ParcelsCategory)