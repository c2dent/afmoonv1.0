# Generated by Django 2.2.5 on 2020-03-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avtomobil',
            name='isMileage',
            field=models.BooleanField(default=True, verbose_name='С Пробегом'),
        ),
    ]
