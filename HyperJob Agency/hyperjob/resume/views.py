from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.http import HttpResponse, HttpResponseForbidden


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lists.html', context={'name': 'Resumes', 'lists': Resume.objects.all()})


class CreateResumeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                return render(request, 'create.html', context={'mode': 'Resume'})
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                description = request.POST.get('description')
                Resume.objects.create(author=request.user, description=description)
                return redirect('/home')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
