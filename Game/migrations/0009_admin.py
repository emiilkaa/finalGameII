# Generated by Django 3.1 on 2021-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0008_auto_20210227_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.IntegerField(verbose_name='Day')),
            ],
        ),
    ]
