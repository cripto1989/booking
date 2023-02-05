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


class Event(TimeStampedModel):

    class EventType(models.TextChoices):
        PUBLIC =  "Public"
        PRIVATE = "Private"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=EventType.choices, default=EventType.PUBLIC)

    def __str__(self) -> str:
        return f"{self.id}({self.type})"


class Booking(TimeStampedModel):

    class BookingStatus(models.TextChoices):
        ACTIVE = "Active"
        CANCELED = "Canceled"  # In case of a lazy delete

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=BookingStatus.choices, default=BookingStatus.ACTIVE)

    def __str__(self) -> str:
        return f"{self.id}"