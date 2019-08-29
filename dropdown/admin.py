from django.contrib import admin
from .models import Department, Subject, Person

# Register your models here.
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Person)
