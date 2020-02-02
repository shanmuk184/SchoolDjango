from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager

class Subject(models.Model):
    name = models.CharField(max_length=64)

class User(models.Model):
    name = models.CharField(max_length=64)
class School(models.Model):
    '''
        subjects
        class_rooms
        teachers
        subjects
        students
    '''
    name = models.CharField(max_length=64)
    # student = models.ManyToManyField(User, through='Student', through_fields=('school', 'user'), related_name='students')
    # subject = models.ManyToManyField(Subject, through='SubjectMapping', through_fields=('school', 'subject'))
    # teacher = models.ManyToManyField(User, through='Teacher', through_fields=('school', 'user'), related_name='teachers')
    # classe = models.ManyToManyField(Class, through='ClassMapping', through_fields=('school', 'class_id'))


class Class(models.Model):
    name = models.CharField(max_length=64)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Teacher(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doj = models.DateField()
    salary_per_annum  = models.FloatField()
    web_lecture_capability = models.IntegerField(choices=Answer.choices)
    subjects = models.ManyToManyField(Subject)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class ClassMapping(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    # subject = models.ManyToManyField(Subject, through='SubjectMapping', through_fields=('class_id', 'subject'))
    # student = models.ManyToManyField(User, through='Student', through_fields=('cls', 'user'))


class SubjectMapping(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_id =    models.ForeignKey(Class, on_delete=models.CASCADE, name='class', related_name='classes')
    per_class_duration = models.IntegerField()
    totalDuration = models.IntegerField()
    taught_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Student(models.Model):
    doj = models.DateField()
    standard = models.IntegerField()
    roll_num = models.IntegerField()
    ranking = models.IntegerField()
    cls = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)