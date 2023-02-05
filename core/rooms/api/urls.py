from django.urls import path
from .views import EventView, RoomView

urlpatterns = [    
    path("room/", RoomView.as_view(), name="create_room"),
    path("event/", EventView.as_view(), name="create_event"),
]