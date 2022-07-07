from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from apps.exercise.models import MaximExercise, Category, Exercise


@register(MaximExercise)
class MaximExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'exercise_id', 'maxim')


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


@register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'formula', 'url')
