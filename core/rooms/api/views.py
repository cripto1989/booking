from rest_framework.generics import CreateAPIView
from .serializers import EventSerializer, RoomSerializer
from rooms.models import Event, Room


class RoomView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
