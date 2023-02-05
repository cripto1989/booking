from rest_framework.generics import CreateAPIView
from .serializers import BookingSerializer, EventSerializer, RoomSerializer
from rooms.models import Booking, Event, Room


class RoomView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class BookingView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
