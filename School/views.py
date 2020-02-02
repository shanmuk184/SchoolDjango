from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from .models import School, Class, Teacher
from django.http import HttpResponse
from django.template import loader
from .options import school_options, class_options, student_options
from .forms import SchoolForm, ClassForm, StudentForm, SubjectForm

# Create your views here.

def create_school(request):
    """
    This is a form
    """
    template = loader.get_template('form.html')
    form = SchoolForm()
    return HttpResponse(template.render({'form':form, 'redirect':'/school', 'submit':'Create School'}, request))


def create_cls(request):
    """
    This is a form
    """
    template = loader.get_template('form.html')
    form = ClassForm()
    return HttpResponse(template.render({'form':form, 'redirect': '/class', 'submit':'Create Class'}, request))


def create_student(request):
    """
    This is a form
    """
    template = loader.get_template('form.html')
    form = StudentForm()
    return HttpResponse(template.render({'form':form, 'redirect': '/student', 'submit':'Create Student'}, request))


def create_subject(request):
    """
    This is a form
    """
    template = loader.get_template('form.html')
    form = SubjectForm()
    return HttpResponse(template.render({'form':form, 'redirect': '/class', 'submit':'Create Subject and add to class'}, request))


def cls(request):
    template = loader.get_template('class.html')
    context = {}
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()

    context['options'] = class_options
    return HttpResponse(template.render(context, request))

def student(request):
    template = loader.get_template('index.html')
    context = {}
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()

    context['options'] = student_options
    return HttpResponse(template.render(context, request))



def teachers_list(request):
    teachers = Teacher.objects.all()

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def create_school_page(request):
    template = loader.get_template('createschool.html')
    return HttpResponse(template.render({}, request))

def schoollist(request):

    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'options':school_options
    }
    template = loader.get_template('school.html')
    return HttpResponse(template.render(context, request))

#
# def get_teachers(request):
#     teachers =