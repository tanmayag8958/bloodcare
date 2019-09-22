from django.contrib import admin
from .models import Address, UserDetails, HospitalDetails, BankDetails, DoantionLogDetails

# Register your models here.
admin.site.register(Address)
admin.site.register(UserDetails)
admin.site.register(HospitalDetails)
admin.site.register(BankDetails)
admin.site.register(DoantionLogDetails)
