from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from .models import Courses,Details


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def courses(request):
    ac = Courses.objects.all()
    context = {'ac' : ac}
    return render (request,'resources.html',context)

def details(request,course_id):
    try:
        course = Courses.objects.get(pk=course_id)
    except Courses.DoesNotExist:
        raise Http404("Course Not Available")
    return render (request, 'detail.html',{'course': course})
