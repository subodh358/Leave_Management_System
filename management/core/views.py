from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from .forms import EmployeeSignUpForm, ManagerSignUpForm, AdminSignUpForm
from .models import Staff, Employee, Manager
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .decorators import *
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie



@unauthenticated
def employee_login(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        username = request_data['username']
        password = request_data['password']
        print(request.user)
        guest = authenticate(request, username=username, password=password )
        if guest is not None and guest.role is Staff.EMPLOYEE:
            login(request, guest)
            return JsonResponse({"success": True, "message": "employee loged in successfully"})
        else:
            return JsonResponse({"success": False, "message": "invalid employee details"})
    

@unauthenticated
def manager_login(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        username = request_data['username']
        password = request_data['password']
        guest = authenticate(request, username=username, password=password)
        if guest is not None and guest.role is Staff.MANAGER:
            login(request, guest)
            return JsonResponse({"success": True, "message": "manager loged in successfully"})
        else:
            return JsonResponse({"success": False, "message": "invalid manager details"})


@unauthenticated
def employee_registeration(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        mgr_id = request_data['manager_id']
        my_manager = Manager.objects.get(manager_id=mgr_id)
        request_data['my_manager'] = my_manager
        form = EmployeeSignUpForm(request_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "employee registration successful"})
        else:
            return JsonResponse({"success": False, "message": "invalid employee details"})


@unauthenticated
def manager_registeration(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        form = ManagerSignUpForm(request_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "manager registration successful"})
        else:
            return JsonResponse({"success": False, "message": "invalid manager details", "errors": form.errors})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')





@unauthenticated
def admin_registeration(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        form = AdminSignUpForm(request_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "admin registration successful"})
        else:
            return JsonResponse({"success": False, "message": "invalid admin details", "errors": form.errors})

@unauthenticated
def admin_login(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        username = request_data['username']
        password = request_data['password']
        print(request.user)
        guest = authenticate(request, username=username, password=password )
        if guest is not None and guest.role is Staff.ADMIN:
            login(request, guest)
            return JsonResponse({"success": True, "message": "admin loged in successfully"})
        else:
            return JsonResponse({"success": False, "message": "invalid admin details"})
    