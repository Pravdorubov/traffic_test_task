from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def get_employer_data(employer):
    emp_dict = {
        "name" : employer.name,
        "date" : employer.date_employment,
        "salary" : employer.salary,
        "duty": employer.duty
    }
    return emp_dict

def get_dep_data(deps, sup_dep_list):
    for dep in deps:
        dep_dict = {}
        dep_dict["name"] = dep.name
        dep_emps = [get_employer_data(e) for e in Employer.objects.filter(duty__department=dep).order_by()]
        dep_dict["employers"] = dep_emps
        sub_deps = [d for d in Department.objects.filter(major_id=dep.id)]
        dep_dict["sub_depts"] = []
        if len(sub_deps) > 0:
            get_dep_data(sub_deps, dep_dict["sub_depts"] )
        sup_dep_list.append(dep_dict)

# def index(request):
#     data = {}
#     data["majors"] = []
#     major_deps =[d for d in Department.objects.filter(level=1)]
#     for md in major_deps:
#         get_dep_data(major_deps, data["majors"])
#     context = {
#         "data" : data
#     }
#     return render(request, "ttt/index.html", context)

def index(request):
    context = {
        "data" : [d for d in Department.objects.filter(level=1)]
    }
    return render(request, "ttt/index.html", context)

def load(request, dep_id):
    context = {
        "data" : Department.objects.get(id = dep_id)
    }
    return render(request, "ttt/load.html", context)