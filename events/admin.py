from django.contrib import admin
from .models import Event, Registration

# This tells Django to show these tables in the admin dashboard
admin.site.register(Event)
admin.site.register(Registration)