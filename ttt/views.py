from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def index(request):

    dep_list = Department.objects.all()
    context = {
        "dep_list": dep_list
    }
    return render(request, "ttt/index.html", context)