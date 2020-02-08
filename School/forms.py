from django import forms
from .models import School, Student, Class
from django.utils.translation import gettext_lazy as _


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['name']
        labels = {
            'name':_('School Name')
        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        labels = {
            'name': _('Class Name'),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            'name': _('Class Name'),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"
        labels = {
            'name': _('Class Name'),
        }

class TeacherSearchForm(forms.ModelForm):
    teacher_name = forms.CharField(name='Teacher name')