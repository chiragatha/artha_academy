from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Courses, Details, Subject


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def courses(request):
    ac = Courses.objects.filter(std__startswith='2')
    context = {'ac' : ac}
    return render (request,'courses.html',context)

def details(request,course_id):
    try:
        course = Courses.objects.get(pk=course_id)
    except Courses.DoesNotExist:
        raise Http404("Course Not Available")
    return render (request, 'detail.html',{'course': course})

def subjects(request):
    sub = Subject.objects.all()
    context = {'sub' : sub}
    return render (request,'detail.html',context)

def calendar(request):
    return render(request,'calendar.html')
def search(request):
    return render(request,'search.html')
def faqs(request):
    return render(request,'faq.html')
def settings(request):
    return render(request,'settings.html')
