# Generated by Django 2.2.12 on 2020-07-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='standard',
            field=models.CharField(default='', max_length=30, verbose_name='username'),
        ),
    ]
