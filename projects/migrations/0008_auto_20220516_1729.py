# Generated by Django 2.2.12 on 2022-05-16 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_project_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
