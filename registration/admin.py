from django.contrib import admin

# Register your models here.
from .models import Register, Instructions

admin.site.register(Register)
admin.site.register(Instructions)
