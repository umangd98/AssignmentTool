# Generated by Django 3.1.3 on 2020-11-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
        ('Class', '0003_auto_20201108_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='Students.Student'),
        ),
    ]