from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .managers import ClassManager,  StudentManager

class User(models.Model):
    name = models.CharField(max_length=64)
    class Meta:
        abstract=True

class Teacher(models.Model):
    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')
    name = models.CharField(max_length=64)
    doj = models.DateField()
    salary_per_annum  = models.FloatField()
    web_lecture_capability = models.IntegerField(choices=Answer.choices)
    def __str__(self):
        return self.name
#
class Subject(models.Model):
    name = models.CharField(max_length=64)
    per_class_duration = models.IntegerField()
    totalDuration = models.IntegerField()

class ClassRoom(models.Model):
    name = models.CharField(max_length=64)

class SubjectMapping(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    cls = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='subjects')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    manager = ClassManager()
    def __str__(self):
        return "%s (%s)" % (
            self.subject.name,
            self.teacher.name
        )

class Student(models.Model):
    doj = models.DateField()
    standard = models.IntegerField()
    roll_num = models.IntegerField()
    ranking = models.IntegerField()
    name = models.CharField(max_length=64)
    cls = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    manager = StudentManager()
    def __str__(self):
        return self.name

admin.site.register(Student)
# admin.site.register(User)
# admin.site.register(Class)
# admin.site.register(School)
# admin.site.register(Subject)
# admin.site.register(ClassRoom)