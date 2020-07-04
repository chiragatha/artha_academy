from django.contrib import admin

# Register your models here.
from .models import Courses,Details,Lectures,Notes

admin.site.register(Courses)
admin.site.register(Details)
admin.site.register(Lectures)
admin.site.register(Notes)

