# Generated by Django 4.0 on 2023-01-19 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredients',
            new_name='ingredients',
        ),
    ]