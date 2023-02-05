from django.urls import path
from .views import BookingView, EventView, RoomView, CancelBookingView

urlpatterns = [    
    path("room/", RoomView.as_view(), name="create_room"),
    path("event/", EventView.as_view(), name="create_event"),
    path("booking/cancel/<uuid:id>/", CancelBookingView.as_view(), name="cancel_booking"),
    path("booking/", BookingView.as_view(), name="create_booking"),
]