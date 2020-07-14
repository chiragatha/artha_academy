from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import RegisterationForm

def registeration_view(request):
    context ={}
    if request.POST:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registeration_form'] = form
    else:
        form = RegisterationForm()
        context['registeration_form']=form
    return render (request,'register.html',context)



