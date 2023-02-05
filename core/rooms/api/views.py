from rest_framework.generics import CreateAPIView
from .serializers import RoomSerializer
from rooms.models import Room


class RoomView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
