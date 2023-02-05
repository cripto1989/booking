import uuid
from django.db import models
from model_utils.models import TimeStampedModel


class Room(TimeStampedModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    capacity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"Room {self.id} with capacity {self.capacity}"