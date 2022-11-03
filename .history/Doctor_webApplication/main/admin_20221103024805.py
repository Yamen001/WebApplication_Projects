from django.contrib import admin
from .models import username, password, phone_number, Gender

# Register your models here.

admin.site.register(username)
admin.site.register(password)
admin.site.register(phone_number)
admin.site.register(BookInstance)
