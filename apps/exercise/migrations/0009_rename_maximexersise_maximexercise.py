# Generated by Django 4.0.5 on 2022-07-05 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_telegramuser_pronation_and_more'),
        ('exercise', '0008_exercise_formula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaximExersise',
            new_name='MaximExercise',
        ),
    ]