from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    author = models.ForeignKey(User, related_name="author_resume", on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

