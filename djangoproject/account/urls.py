from django.urls import path

from .views import registeration_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('register/',registeration_view, name="register")
]