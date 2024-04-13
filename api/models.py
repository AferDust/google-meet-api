from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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


class Bank(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class BankCardType(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=1024)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class CashBack(models.Model):
    expired_date = models.DateField(null=True, blank=True)
    percent = models.FloatField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    card_type = models.ForeignKey(BankCardType, on_delete=models.CASCADE)

    def is_expired(self):
        return self.expired_date < timezone.now().date()

    def __str__(self):
        return f"{self.percent}% until {self.expired_date}"


class Card(models.Model):
    number = models.CharField(max_length=19)
    expired_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.ForeignKey(BankCardType, on_delete=models.CASCADE)

    def is_expired(self):
        return self.expired_date < timezone.now().date()

    def __str__(self):
        return f"{self.number} - Expires on {self.expired_date}"

