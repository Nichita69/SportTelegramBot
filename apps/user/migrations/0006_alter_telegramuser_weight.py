# Generated by Django 4.0.5 on 2022-06-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_telegramuser_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='weight',
            field=models.FloatField(default=50, max_length=150),
        ),
    ]
