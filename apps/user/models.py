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

    bench_presss = models.FloatField(null=False, default=80)
    dumbell_press = models.FloatField(null=False, default=80)
    bars = models.FloatField(null=False, default=80)
    elastic = models.FloatField(null=False, default=80)
    twisting_rod = models.FloatField(null=False, default=80)
    biceps_seet = models.FloatField(null=False, default=80)
    dead_lifting_finger = models.FloatField(null=False, default=80)
    block_arm = models.FloatField(null=False, default=80)
    luchevaya = models.FloatField(null=False, default=80)
    biceps_stay = models.FloatField(null=False, default=80)
    block_pull = models.FloatField(null=False, default=80)
    ugal_biceps = models.FloatField(null=False, default=80)
    Pronation = models.FloatField(null=False, default=80)
    otvedenie = models.FloatField(null=False, default=80)
    giri = models.FloatField(null=False, default=80)
    army_presss = models.FloatField(null=False, default=80)
    dumbell_prees_stayted= models.FloatField(null=False, default=80)
    leg_press = models.FloatField(null=False, default=80)


class MaximExersise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=TelegramUser, null=False, on_delete=models.CASCADE)
    exercise = models.ForeignKey(to=Exercise, null=False, on_delete=models.CASCADE)
    maxim = models.FloatField(null=False, default=150)
