from django.contrib import admin
from .models import Register

# Register your models here.
admin.site.unregister(Group)

admin.site.register(Register)
