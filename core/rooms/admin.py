from django.contrib import admin
from .models import Booking, Room, Event

admin.site.register(Room)
admin.site.register(Event)
admin.site.register(Booking)
