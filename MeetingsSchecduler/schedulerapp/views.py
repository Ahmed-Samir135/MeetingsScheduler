import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Appointment, Manager, Secretary
from .forms import AppointmentForm


def index(request):
    
    if request.user.is_secretary:
        temp = "schedulerapp/index_secretary.html"
    else:
        temp = "schedulerapp/index_manager.html"
    return render(request, temp)

def appointment_list(request):

    current_user = request.user
    appointments = []
    if current_user.is_authenticated:
        if current_user.is_secretary:
            appointments = Appointment.objects.filter(secretary_id=current_user.id)
        elif request.user.is_manager:
            manager = Manager.objects.get(pk=current_user.id)
            secretay = Secretary.objects.get(manager_id=current_user.id)
            appointments = Appointment.objects.filter(secretary_id=secretay.pk)

    colors = {"إنتظار": "#ffc107", "دخول": "#198754","قدوم":"white","تأجيل":"#adb5bd","إلغاء":"#dc3545"}
    
    if request.user.is_secretary:
        temp = "schedulerapp/appointment_list_secretary.html"
    else:
        temp = "schedulerapp/appointment_list_manager.html"
    return render(
        request,
        temp,
        {
            "appointments": appointments,
            "StatusColor": colors,
        },
    )


@login_required
def profile(request):
    return render(request, "users/profile.html")