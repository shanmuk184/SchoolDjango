from django.db import models
from django.utils.translation import gettext_lazy as _
# class SubjectManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().prefetch_related('classes__students', 'teacher')

class ClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('teacher','cls')

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('cls')
