from django.contrib import admin

# Register your models here.
from .models import User,TeamRegistration

admin.site.register(User)
admin.site.register(TeamRegistration)