# Generated by Django 4.0 on 2022-11-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='city',
        ),
        migrations.RemoveField(
            model_name='users',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='users',
            name='description',
        ),
        migrations.RemoveField(
            model_name='users',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='users',
            name='experience',
        ),
    ]