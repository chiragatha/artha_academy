from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('resources',views.Resources.as_view(),name= 'resources'),
]