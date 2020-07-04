from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('resources',views.courses,name= 'resources'),
    path('resources/<int:course_id>/',views.details, name = 'details'),
]