from django import forms
from jobapp.models import Category,job
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

class JobForm(forms.ModelForm):
    class Meta:
        model=job
        #exclude=('salary',)
        fields='__all__'