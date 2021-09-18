from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ResumeModel)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin','mobile','email','job_city','profile_image','resume']
