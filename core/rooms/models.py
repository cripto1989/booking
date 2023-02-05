import uuid
from enum import Enum
from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


class Room(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    capacity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id}({self.capacity})"


class EventType(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"

    @classmethod
    def choices(cls):
        return [(type_event.name, type_event.value) for type_event in cls]


class Event(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=EventType.choices(), default=EventType.PUBLIC)

    def __str__(self) -> str:
        return f"{self.id}({self.type})"


class BookingStatus(Enum):
    ACTIVE = "Active"
    CANCELED = "Canceled"

    @classmethod
    def choices(cls):
        return [(booking_status.name, booking_status.value) for booking_status in cls]


class Booking(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=BookingStatus.choices(), default=BookingStatus.ACTIVE)

    def __str__(self) -> str:
        return f"{self.id}"