# Generated by Django 4.0 on 2022-11-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_quotes_description_alter_quotes_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='userName',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotes',
            name='userTatto',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]