# Generated by Django 4.1.7 on 2023-03-19 07:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(10)]
            ),
        ),
        migrations.AlterField(
            model_name="blog", name="date", field=models.DateField(auto_now=True),
        ),
    ]
