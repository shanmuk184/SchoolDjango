from django.urls import path
from .views import *
# views = AssignmentViews()
urlpatterns=[
    path('', schoollist, name='index'),
    path('school', schoollist, name='school'),
    path('create_school', create_school, name= 'create_school'),
    path('class', cls, name = 'class'),
    path('createclass', create_cls, name= 'create_class'),
    path('student', student, name='student'),
    path('subject', subject, name='subject'),
    path('createstudent', create_student, name='create_student'),
    path('createsubjectinclass', create_subject, name='create_subject_in_class'),
    path('api/school/classes', schoolclassesandsubjects, name='school_classes_subjects_api'),
    path('school/classes', tableSchoolclassesandsubjects, name='school_classes_subjects'),
    path('api/teacher/high', getNoOfStudentsTaughtByTeachersEarningMoreThanOne, name='getNoOfStudentsTaughtByTeachersEarningMoreThanOne'),
    path('api/subjects/taught', get_total_duration_of_subject_teachers_more_than_one, name ='get_total_duration_of_subject_teachers_more_than_one'),
    path('studentsearch', getStudentDetailsBasedOnTeacherDetails, name="getStudentDetailsBasedOnTeacherDetails")
]