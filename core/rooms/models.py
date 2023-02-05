import uuid
from enum import Enum
from django.db import models
from model_utils.models import TimeStampedModel


class Room(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    capacity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id} with capacity {self.capacity}"


class EventType(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"

    @classmethod
    def choices(cls):
        return [(type_event.name, type_event.value) for type_event in cls]


class Event(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    models.CharField(max_length=10, choices=EventType.choices())

    def __str__(self) -> str:
        return f"{self.id} in room {self.room.id}"