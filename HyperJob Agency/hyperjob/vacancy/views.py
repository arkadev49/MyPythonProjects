from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseForbidden
from vacancy.models import Vacancy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html', context={'auth': request.user.is_authenticated})


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lists.html', context={'name': 'Vacancy', 'lists': Vacancy.objects.all()})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class ProfilePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', context={'username': request.user.username,
                                                     'pos': "Manager" if request.user.is_staff else "Candidate",
                                                     'is_staff': request.user.is_staff,
                                                     'auth': request.user.is_authenticated})


class CreateVacancyView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, 'create.html', context={'mode': 'Vacancy'})
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                description = request.POST.get('description')
                Vacancy.objects.create(author=request.user, description=description)
                Vacancy.save()
                return redirect('/home')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
