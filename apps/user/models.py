from django.db import models

from apps.exercise.models import Exercise


class TelegramUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    chat_id = models.CharField(max_length=255, unique=True)
    weight = models.FloatField(null=False, default=50, max_length=3)
    height = models.FloatField(null=False, default=70)


class MaximExersise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=TelegramUser, null=False, on_delete=models.CASCADE)
    exercise = models.ForeignKey(to=Exercise, null=False, on_delete=models.CASCADE)
    maxim = models.FloatField(null=False, default=150)
