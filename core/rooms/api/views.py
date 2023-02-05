from django.http import Http404
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import BookingSerializer, EventSerializer, RoomSerializer
from rooms.models import Booking, Event, Room


class RoomView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
     

class DeleteRoomView(DestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()    
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        room = self.get_object()
        if room.event_set.all():
            return Response({"message": "There is at least an event related to this room"}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class BookingView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class CancelBookingView(DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    lookup_field = "id"
