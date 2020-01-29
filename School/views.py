from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from .models import School, Class, Teacher

# Create your views here.

def create_school(request):
    school_name=request.GET['name']

    school = School.objects.create(name=school_name)
    return JsonResponse(school.id, safe=False)

def create_class(request):
    class_name = request.GET['name']
    school_id = request.GET['school_id']
    school = School.objects.get(id=school_id)
    cls = Class.objects.get_or_create(name=class_name)
    school.classes.add(cls[0].id)
    return JsonResponse([cls.name for cls in school.classes.all()], safe=False)

def teachers_list(request):
    teachers = Teacher.objects.all()

#
# def get_teachers(request):
#     teachers =