from django.contrib import admin
from .models import Emp
class EmpAdmin(admin.ModelAdmin):
    list_display = ['name','id']
# Register your models here.
admin.site.register(Emp,)