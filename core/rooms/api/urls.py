from django.urls import path
from .views import BookingView, EventView, RoomView

urlpatterns = [    
    path("room/", RoomView.as_view(), name="create_room"),
    path("event/", EventView.as_view(), name="create_event"),
    path("booking/", BookingView.as_view(), name="create_booking"),
]