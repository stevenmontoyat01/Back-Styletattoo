# Generated by Django 4.0 on 2022-11-21 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tatto', '0003_alter_tattoo_artist_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tattoo_artist',
            name='like',
        ),
    ]
