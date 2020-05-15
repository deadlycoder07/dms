from django.contrib import admin

# new
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

admin.site.register(CustomUser)



class HospitalAdmin(UserAdmin):
    add_form = HospitalForm
    form = HospitalChangeForm
    model = Hospital
    list_display = ['name', 'registration_no', 'address', 'phone', 'beds']

admin.site.register(Hospital)



class ClinicAdmin(UserAdmin):
    add_form = ClinicForm
    form = ClinicChangeForm
    model = Clinic
    list_display = ['name', 'registration_no', 'address', 'phone',]

admin.site.register(Clinic)
