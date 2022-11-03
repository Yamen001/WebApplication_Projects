from django.contrib import admin
from .models import username, password, phone_number, Gender

# Register your models here.

admin.site.register(username)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
