from django.db import models
from users.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    repo_url = models.URLField(max_length=200)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
