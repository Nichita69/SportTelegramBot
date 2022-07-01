# Generated by Django 4.0.5 on 2022-07-01 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_delete_maximexersise'),
        ('exercise', '0006_remove_exercise_maxim'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaximExersise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maxim', models.FloatField(default=150)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.telegramuser')),
            ],
        ),
    ]
