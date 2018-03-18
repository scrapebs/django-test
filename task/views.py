from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import resolve_url
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import mail_admins, send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Sending_Info
from .forms import UserRegistrationForm


def index(request):
    if request.method == 'POST':
        email_from = request.POST.get('email_from')
        email_text = request.POST.get('email_text')
        check = send_mail("Message from " + email_from, 
                          email_text, email_from,  
                          ['denissinkov@mail.ru'], 
                          fail_silently=True)
        if check == 1:
            message = Sending_Info(email_from=email_from, 
                                   sending_status=True, 
                                   created_date=timezone.now())
            message.save()
            return HttpResponse('fine')
        else:
            message = Letter(email_from=email_from, 
                             sending_status=False, 
                             created_date=timezone.now())
            message.save()
            return HttpResponse('bad')
    else:
        return render(request, 'task/index.html', )

def authorization(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('fine')
            else:
                return HttpResponse('inactive')
        else:
            return HttpResponse('bad')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html',{'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponse('fine')
        else:   
            return HttpResponse('bad')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html',{'form': form})