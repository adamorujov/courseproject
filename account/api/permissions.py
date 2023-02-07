from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.course.accounts.all() and request.user.category == "T"
    
class IsTeacherUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.category == "T"

class IsStudentUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.category == "S"
    
    
