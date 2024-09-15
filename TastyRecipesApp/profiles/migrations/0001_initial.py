# Generated by Django 5.1.1 on 2024-09-15 02:47

import TastyRecipesApp.profiles.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(error_messages={'unique': 'Nickname must be at least 2 chars long!'}, max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=30, validators=[TastyRecipesApp.profiles.validators.validate_user_names])),
                ('last_name', models.CharField(max_length=30, validators=[TastyRecipesApp.profiles.validators.validate_user_names])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
