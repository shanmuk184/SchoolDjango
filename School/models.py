from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager
from django.contrib import admin
class SubjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('classes__students', 'teachers__user')


class Subject(models.Model):
    name = models.CharField(max_length=64)
    per_class_duration = models.IntegerField()
    totalDuration = models.IntegerField()
    manager=SubjectManager()


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

class ClassRoom(models.Model):
    name = models.CharField(max_length=64)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # student = models.ManyToManyField(User, through='Student', through_fields=('cls', 'user'))
    # subject = models.ManyToManyField(Subject, through='Class', through_fields=('classes', 'subject'))

class Teacher(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doj = models.DateField()
    salary_per_annum  = models.FloatField()
    web_lecture_capability = models.IntegerField(choices=Answer.choices)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class ClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('cls__school', 'subject', 'taught_by__user').filter(cls__school_id=1)

class Class(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    cls = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    taught_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    manager = ClassManager()
    def __str__(self):
        return "%s (%s) (%s)" % (
            self.cls.name,
            self.subject.name,
            self.taught_by.user.name
        )

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('user')

class Student(models.Model):
    doj = models.DateField()
    standard = models.IntegerField()
    roll_num = models.IntegerField()
    ranking = models.IntegerField()
    cls = models.ManyToManyField(Class, related_name='students')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager = StudentManager()
    def __str__(self):
        return self.user.name


admin.site.register(Student)
admin.site.register(User)
admin.site.register(Class)
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(ClassRoom)