# Generated by Django 2.2.12 on 2022-05-16 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='score',
        ),
    ]
