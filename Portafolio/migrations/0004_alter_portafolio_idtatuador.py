# Generated by Django 4.0 on 2022-11-21 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('Portafolio', '0003_rename_portafolio_portafolio_idtatuador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='idTatuador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Portafolio', to='accounts.users'),
        ),
    ]
