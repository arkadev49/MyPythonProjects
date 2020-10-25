"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from vacancy.views import MainPageView
from resume.views import ResumesView, CreateResumeView
from vacancy.views import VacancyView, SignUpView, UserLoginView, ProfilePageView, CreateVacancyView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('resumes/', RedirectView.as_view(url='/resumes')),
    path('vacancies/', RedirectView.as_view(url='/vacancies')),
    path('resumes', ResumesView.as_view()),
    path('vacancies', VacancyView.as_view()),
    path('login/', RedirectView.as_view(url='login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', SignUpView.as_view()),
    path('login', UserLoginView.as_view()),
    path('resume/new/', RedirectView.as_view(url='/resume/new')),
    path('vacancies/new/', RedirectView.as_view(url='/vacancy/new')),
    path('vacancy/new', CreateVacancyView.as_view()),
    path('resume/new', CreateResumeView.as_view()),
    path('home', ProfilePageView.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
    path('logout', LogoutView.as_view()),
    path('home/', RedirectView.as_view(url='/logout')),
]
