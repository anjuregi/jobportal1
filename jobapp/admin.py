from django.contrib import admin

# Register your models here.
from jobapp.models import job,Category
admin.site.register(job)
admin.site.register(Category)