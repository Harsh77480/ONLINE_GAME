# Generated by Django 3.2.3 on 2021-05-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_game_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='word',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]
