from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from core.decorators import employee, manager, unauthenticated, admin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .forms import LeaveApplicationForm
from leaves.models import LeaveApplication
from django.core import serializers

def get_formatted_data(application_list):
    json_list = []
    for al in application_list:
        data = {
            "description": al.description,
            "status": al.status
        }
        json_list.append(data)
    return json_list




@login_required
@manager
def application_list(request):
    if request.method =="GET":
        manager = request.user.id
        application_list = LeaveApplication.objects.filter(author__my_manager__id=manager)
        data = {
            'data': get_formatted_data(application_list)
        }
        return JsonResponse(data)


@login_required
@manager
def application_status(request, pk):
    if request.method == "POST":
        request_data = json.loads(request.body)
        changed_status = request_data['status']
        x = LeaveApplication.objects.get(id=pk)
        x.status = changed_status
        x.save()
        return JsonResponse({"status_changed": True})
    else:
        return JsonResponse({"status_changed": False})


@login_required
@employee
def application_create(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        request_data['author'] = request.user
        form = LeaveApplicationForm(request_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message":"application created.."})
        else:
            return JsonResponse({"success": False, "message": "cant create applicaion", "errors":form.errors})


@login_required
@employee
def available_leaves(request):
    if request.method == "POST":
        y = request.user
        lst = y.LeaveApplicationForm.objects.filter(status='approved').count()
        leaves_remain = 14 - lst
        return JsonResponse({"available_leaves": leaves_remain})
#-------------------------->
def get_formatted_data_admin(applications):
    json_list = []
    for al in applications:
        data = {
            "description": al.description,
            "status": al.status,
            "user": al.author
        }
        json_list.append(data)
    return json_list


@login_required
@admin
def track_applications(request):
    if request.method == "POST":
        applications = LeaveApplicationForm.objects.get.all()
        data = {
            'data': get_formatted_data_admin(applications)
        }
        return JsonResponse(data)

