# Generated by Django 2.2.12 on 2020-07-15 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artha', '0006_courses_standard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='standard',
        ),
    ]
