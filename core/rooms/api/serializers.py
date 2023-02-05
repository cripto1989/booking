from rest_framework import serializers
from rooms.models import Booking, Event, Room, EventType, BookingStatus


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"

    def validate_capacity(self, value):        
        if value <= 0:
            raise serializers.ValidationError("Capacity should be greater that 0")
        return value


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

    def validate_event(self, value):        
        if value.type.title() == EventType.PRIVATE.value:
            raise serializers.ValidationError(f"You cannot reserve for private events")
        if not self._is_there_availability(value):
            raise serializers.ValidationError(f"There is not more space available for this event")
        return value

    def _is_there_availability(self, event):
        reservations = Booking.objects.filter(event=event, status=BookingStatus.ACTIVE.value.upper()).count()                
        return reservations < event.room.capacity
