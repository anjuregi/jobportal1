from django import forms
from django.contrib.auth.models import User
class HrRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","first_name","last_name","email"]
class HrLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
