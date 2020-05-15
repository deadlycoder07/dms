from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


#form for hospital regn
class HospitalForm(UserCreationForm):

    class Meta:
        model = Hospital
        fields = ('name', 'registration_no', 'address', 'phone', 'beds')

class HospitalChangeForm(UserChangeForm):

    class Meta:
        model = Hospital
        fields = UserChangeForm.Meta.fields

#form for clinic regn
class ClinicForm(UserCreationForm):

    class Meta:
        model = Clinic
        fields = ('name', 'registration_no', 'address', 'phone')


class ClinicChangeForm(UserChangeForm):

    class Meta:
        model = Clinic
        fields = UserChangeForm.Meta.fields
