from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookingSerializer, EventSerializer, RoomSerializer
from rooms.models import Booking, Event, Room
from rooms.api.permissions import CanBooking, IsOwnerOfBooking


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
            return Response(
                {"message": "There is at least an event related to this room"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


class EventView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventsView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(type=Event.EventType.PUBLIC)


class BookingView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [CanBooking]

    def create(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CancelBookingView(DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsOwnerOfBooking]
    lookup_field = "id"
