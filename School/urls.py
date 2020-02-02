from django.urls import path
from .views import create_school, create_cls, index, schoollist, create_student, student, cls, create_subject
urlpatterns=[
    path('', index, name='index'),
    path('school', schoollist, name='school'),
    path('create_school', create_school, name= 'create_school'),
    path('class', cls, name = 'class'),
    path('createclass', create_cls, name= 'create_class'),
    path('student', student, name='student'),
    path('createstudent', create_student, name='create_student'),
    path('createsubjectinclass', create_subject, name='create_subject_in_class')
]