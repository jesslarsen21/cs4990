from django.contrib import admin

# Register your models here.
from .models import Tweet, User, Profile

admin.site.register(Tweet)
admin.site.register(Profile)

