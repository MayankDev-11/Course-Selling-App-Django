from django.shortcuts import render, redirect, HttpResponse
from courses.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib import auth


class SignupView(View):

    def get(self, request):
        form = RegistrationForm()

        return render(request,'courses/signup.html', context={'form':form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            if user:
                return redirect('home')
        return render(request,'courses/signup.html', context={'form':form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'courses/login.html',context=context)

    def post(self, request):
        form = LoginForm(request,data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            return redirect("home")
        return render(request, 'courses/login.html',context=context)


def signout(request):
    auth.logout(request)
    return redirect('home')