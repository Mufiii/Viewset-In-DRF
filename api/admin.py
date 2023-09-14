from django.contrib import admin

from api.models import Student

# Register your models here.


@admin.register(Student)
class AdminStu(admin.ModelAdmin):
    list_display = ['id','name','email','city']