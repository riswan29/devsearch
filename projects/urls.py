from django.urls import path
from .views import *
urlpatterns = [
    path('projects/', projects, name='projects'),
    path('projects/<str:pk>', project, name='project'),

]
