# Generated by Django 2.2.12 on 2022-05-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_detaileddescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]