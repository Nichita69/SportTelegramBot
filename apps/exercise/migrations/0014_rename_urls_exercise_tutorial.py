# Generated by Django 4.0.6 on 2022-07-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0013_exercise_urls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='urls',
            new_name='tutorial',
        ),
    ]
