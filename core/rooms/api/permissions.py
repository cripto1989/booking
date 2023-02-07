from rest_framework import permissions
from rooms.models import Booking


class IsOwnerOfBooking(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer


class CanBooking(permissions.BasePermission):
    def has_permission(self, request, view):
        event = request.data["event"]
        if Booking.objects.filter(event__id=event, customer=request.user):
            return False
        return True
