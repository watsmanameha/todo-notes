from django.db import models
from users.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    repo_url = models.URLField(max_length=200)
    users = models.ManyToManyField(User)

