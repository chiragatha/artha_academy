# Generated by Django 2.2.12 on 2020-07-10 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artha', '0002_remove_courses_instructor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='lectures',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artha.Subject'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artha.Subject'),
        ),
    ]
