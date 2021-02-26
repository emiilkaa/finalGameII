# Generated by Django 3.1 on 2020-12-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('Name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='name')),
                ('Active_a', models.FloatField(default=100, verbose_name='active_a')),
                ('Active_b', models.FloatField(default=100, verbose_name='active_b')),
                ('Education', models.FloatField(default=0, verbose_name='education')),
                ('Day', models.IntegerField(default=1, verbose_name='day')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
    ]