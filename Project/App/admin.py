from django.contrib import admin
from .models import Hospital,HospitalFacilities,FacilityImages
# Register your models here.

admin.site.register(Hospital)
admin.site.register(HospitalFacilities)
admin.site.register(FacilityImages)

