from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Staff, Manager, Employee
from django.http import JsonResponse

def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == Staff.MANAGER:
            return JsonResponse({"authenticated": True, "message": "user logged in as manager"})
        elif request.user.is_authenticated and request.user.role == Staff.EMPLOYEE:
            return JsonResponse({"authenticated": True, "message": "user logged in as employee"})
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

#manager verification decorator
def manager(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == Staff.MANAGER:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"authenticated": True, "message": "user is not manager"})
    return wrapper_func

#employee verification decorator
def employee(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == Staff.EMPLOYEE:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"authenticated": True, "message": "user is not employee"})
    return wrapper_func


#admin
def admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == Staff.ADMIN:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"authenticated": True, "message": "user is not admin"})
    return wrapper_func