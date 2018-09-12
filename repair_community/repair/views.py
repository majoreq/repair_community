from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {
            'form':form
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
                group = Group.objects.get(name=form.cleaned_data['group'])
                # print(form.cleaned_data['group'])
                # print("*")
                # print(group)
                user.save()
                user.groups.add(group)
                return HttpResponse("WORK")


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error = "Wrong username or password"
                return render(request, 'login.html', {'form': form, 'error':error})
        return HttpResponse("Not working")



def logoff(request):
    logout(request)
    return redirect('index')