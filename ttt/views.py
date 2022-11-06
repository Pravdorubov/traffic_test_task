from django.shortcuts import render

from .models import *
def index(request):
    context = {
        "data" : [d for d in Department.objects.filter(level=1)]
    }
    return render(request, "ttt/index.html", context)

def load(request, dep_id):
    data = {}
    data["id"] = dep_id
    duties = [d.id for d in Duty.objects.filter(department_id=dep_id)]
    employers = [e for e in Employer.objects.filter(duty_id__in=duties)]
    data["employers"] = employers
    sub_deps = [ d for d in Department.objects.filter(major_id=dep_id)]
    data_subdeps = []
    for sd in sub_deps:
        sub = {}
        sub["id"] = sd.id
        sub["name"] = sd.name
        data_subdeps.append(sub)
    data["sub_deps"] = data_subdeps
    context = {
        "data" : data
    }
    return render(request, "ttt/load.html", context)