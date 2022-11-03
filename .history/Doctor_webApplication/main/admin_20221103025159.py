from django.contrib import admin
from .models import Register, Users

# Register your models here.
admin.site.unregister(Users)

admin.site.register(Register)
