# Generated by Django 4.0.5 on 2022-06-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_telegramuser_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='weight',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
