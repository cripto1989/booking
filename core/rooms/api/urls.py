from django.urls import path
from .views import BookingView, EventView, EventsView, RoomView, CancelBookingView, DeleteRoomView

urlpatterns = [    
    path("room/delete/<uuid:id>/", DeleteRoomView.as_view(), name="delete_room"),
    path("room/", RoomView.as_view(), name="create_room"),
    path("events/", EventsView.as_view(), name="events"),
    path("event/", EventView.as_view(), name="create_event"),
    path("booking/cancel/<uuid:id>/", CancelBookingView.as_view(), name="cancel_booking"),
    path("booking/", BookingView.as_view(), name="create_booking"),
]