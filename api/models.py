from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(default=None, null=True, blank=True)
    phone_number = models.CharField(default=None, null=True, blank=True)


class Program(models.Model):
    name = models.CharField()
    description = models.TextField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProgramFAQ(models.Model):
    program = models.ForeignKey(Program, related_name='faqs', on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
