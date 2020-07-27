from django.http import request
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import courses, calendar, search, faqs, settings


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('resources/',views.courses,name= 'resources'),
    path('resources/courses/<int:course_id>/',views.details, name = 'details'),
    path('resources/dashboard/',courses, name= 'dashboard'),
    path('resources/courses/',courses, name= 'courses'),
    path('resources/calendar',calendar, name= 'calendar'),
    path('resources/search',search, name= 'search'),
    path('resources/faqs',faqs, name= 'faqs'),
    path('resources/settings',settings, name= 'settings'),


]

urlpatterns += staticfiles_urlpatterns()
