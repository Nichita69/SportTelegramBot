from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from apps.user.models import TelegramUser


@register(TelegramUser)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','chat_id','weight','height')