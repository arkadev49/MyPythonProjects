from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    author = models.ForeignKey(User, related_name="author_vacancy", on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
