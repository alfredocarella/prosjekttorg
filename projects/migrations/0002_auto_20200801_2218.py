# Generated by Django 3.0.7 on 2020-08-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='courses',
            field=models.ManyToManyField(blank=True, to='projects.Course'),
        ),
    ]