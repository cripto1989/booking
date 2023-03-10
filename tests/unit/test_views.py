import pytest
from rest_framework.test import APIClient
from rooms.models import Room, Event, Booking
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create(
        username="user", email="user@domain.com", password="uKzjYF34"
    )


@pytest.fixture
def http_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def room():
    return Room.objects.create(capacity=15)


@pytest.fixture
def event(room):
    return Event.objects.create(room=room)


@pytest.fixture
def booking(event, user):
    return Booking.objects.create(event=event, customer=user)


@pytest.mark.django_db
class TestRoomView:
    def test_create_a_room(self, http_client):
        response = http_client.post("/api/v1.0/room/", {"capacity": "15"})

        assert response.status_code == 201

    def test_delete_a_room(self, http_client, room):
        response = http_client.delete(f"/api/v1.0/room/delete/{str(room.id)}/")

        assert response.status_code == 204


@pytest.mark.django_db
class TestEventView:
    @pytest.mark.parametrize("type_event", [("Public"), ("Private")])
    def test_create_an_event(self, http_client, room, type_event):
        payload = {"room": f"{room.id}", "type": type_event}
        response = http_client.post("/api/v1.0/event/", payload)

        assert response.status_code == 201

    def test_list_all_events(self, http_client, event):
        response = http_client.get("/api/v1.0/events/")

        assert response.status_code == 200
        assert len(response.data) == 1


@pytest.mark.django_db
class TestBookingView:
    def test_create_a_booking(self, http_client, event):
        payload = {"event": f"{event.id}"}

        response = http_client.post("/api/v1.0/booking/", payload)

        assert response.status_code == 201

    def test_cancel_booking(self, http_client, booking):
        response = http_client.delete(f"/api/v1.0/booking/cancel/{booking.id}/")

        assert response.status_code == 204
