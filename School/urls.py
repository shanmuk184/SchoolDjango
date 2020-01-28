from django.urls import path
from .views import create_school, create_class
urlpatterns=[
    path('create_school', create_school, name='create_school'),
    path('create_class', create_class, name = 'create_class')

]