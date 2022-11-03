from django.contrib import admin
from .models import Register

# Register your models here.
admin.site.unregister(Users)

admin.site.register(Register)
