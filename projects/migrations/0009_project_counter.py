# Generated by Django 2.2.12 on 2022-06-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20220516_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]