from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hellllllo dfsgjljkljkjkjkdfsanklmkm");
    """ if request.user.is_secretary:
        temp = "schedulerapp/index_secretary.html"
    else:
        temp = "schedulerapp/index_manager.html"
    return render(request, temp) """
