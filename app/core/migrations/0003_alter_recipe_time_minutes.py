# Generated by Django 4.0 on 2023-01-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(),
        ),
    ]