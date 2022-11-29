# Generated by Django 4.0 on 2022-11-28 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id_quotes', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('img', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=150)),
                ('isActive', models.BooleanField(default=False)),
                ('artist_tattoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfilTattoo', to='accounts.users')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfilUser', to='accounts.users')),
            ],
        ),
    ]
