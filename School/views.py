from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from .models import School, Class, Teacher
from django.http import HttpResponse
from django.template import loader
from .options import school_options, class_options, student_options
from .forms import SchoolForm, ClassForm, StudentForm, SubjectForm, TeacherSearchForm
from .helpers import ModelHelper
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
    return HttpResponse(template.render({'form':form, 'redirect': '/subject', 'submit':'Create Subject and add to class'}, request))


def cls(request):
    template = loader.get_template('class.html')
    context = {}
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
    context['options'] = class_options
    return HttpResponse(template.render(context, request))

def subject(request):
    template = loader.get_template('class.html')
    context = {}
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
    context['options'] = class_options
    return HttpResponse(template.render(context, request))

def student(request):
    template = loader.get_template('index.html')
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
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

helper = ModelHelper()

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



def schoolclassesandsubjects(request):
    classes = helper.getClassesInsideSchool()
    return JsonResponse(classes.values(), safe=False)

def tableSchoolclassesandsubjects(request):
    classes = helper.getClassesInsideSchool()
    context = {
        'entries': classes
    }
    template = loader.get_template('classes.html')
    return HttpResponse(template.render(context, request))

def getNoOfStudentsTaughtByTeachersEarningMoreThanOne(request):
    entries = helper.get_num_students_and_sum_of_teachers_with_salary_gt_twelve()
    context = {
        'students': entries[1],
        'teacher_salaries': entries[0]
    }
    template = loader.get_template('teacher_moe_than_one_lakh.html')
    return HttpResponse(template.render(context, request))



def get_num_students_and_sum_of_teachers_with_salary_gt_twelve(request):
    entries = helper.get_num_students_and_sum_of_teachers_with_salary_gt_twelve()
    return JsonResponse(entries, safe=False)

def get_total_duration_of_subject_teachers_more_than_one(request):
    entries = helper.get_total_duration_of_subject_teachers_more_than_one()
    context = {
        'entries': entries
    }
    template = loader.get_template('subject.html')
    return HttpResponse(template.render(context, request))

def getStudentDetailsBasedOnTeacherDetails(request):
    form = TeacherSearchForm()
    context = {'form':form, 'redirect': '/studentsearch', 'submit':'Get students'}
    template = loader.get_template('studentsearch.html')
    if request.method == 'POST':
        form = TeacherSearchForm(request.POST)
        if form.is_valid():
            students =  helper.search_students_basedon_teacher_name(form.cleaned_data['name'])
            context['students'] = students

    return HttpResponse(template.render(context, request))




#
# def get_teachers(request):
#     teachers =