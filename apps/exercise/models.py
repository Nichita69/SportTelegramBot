from django.db import models

from apps.user.models import TelegramUser


class Category(models.Model):
    category = models.CharField(max_length=150, blank=True, null=True)


class Exercise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    formula = models.CharField(max_length=150, blank=True, null=True)


class MaximExercise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=TelegramUser, null=False, on_delete=models.CASCADE)
    exercise = models.ForeignKey(to=Exercise, null=False, on_delete=models.CASCADE)
    maxim = models.FloatField(null=False, default=150)

    class Meta:
        unique_together = ('user', 'exercise')
