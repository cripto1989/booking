from rest_framework import permissions


class IsOwnerOfBooking(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):        
        return request.user == obj.customer            