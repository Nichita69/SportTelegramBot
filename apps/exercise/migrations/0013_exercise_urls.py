# Generated by Django 4.0.6 on 2022-07-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0012_alter_maximexercise_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='urls',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]
