from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager

class Subject(models.Model):
    name = models.CharField(max_length=64)

class Teacher(models.Model):

    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')

    name = models.CharField(max_length=64)
    doj = models.DateField()
    salary_per_annum  = models.IntegerField()
    web_lecture_capability = models.IntegerField(choices=Answer.choices)
    subjects = models.ManyToManyField(Subject)

class SubjectMapping(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    per_class_duration = models.IntegerField()
    totalDuration = models.IntegerField()
    taught_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=64)
    doj = models.DateField()
    standard = models.IntegerField()
    roll_num = models.IntegerField()
    ranking = models.IntegerField()

class Class(models.Model):
    name = models.CharField(max_length=64)
    subject = models.ManyToManyField(SubjectMapping, )
    students = models.ManyToManyField(Student)

# Create your models here.

# class SchoolManager(models.Manager):
#
#

class School(models.Model):
    '''
        subjects
        class_rooms
        teachers
        subjects
        students
    '''
    name = models.CharField(max_length=64)
    classes = models.ManyToManyField(Class)

