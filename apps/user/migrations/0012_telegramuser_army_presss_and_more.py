# Generated by Django 4.0.5 on 2022-06-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_telegramuser_dumbell_press'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='Army_presss',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='Dumbell_prees_stayted',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='Giri',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='Leg_press',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='Otvedenie',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='Pronation',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='bars',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='biceps_seet',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='biceps_stay',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='block_arm',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='block_pull',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='dead_lifting_finger',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='elastic',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='luchevaya',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='twisting_rod',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='ugal_biceps',
            field=models.FloatField(default=80),
        ),
    ]
