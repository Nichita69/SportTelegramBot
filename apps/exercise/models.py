from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=150, blank=True, null=True)


class Exercise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)



