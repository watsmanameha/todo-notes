from django.db import models

from users.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=64, unique=True)
    repo_url = models.URLField(max_length=200, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.project_name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project
