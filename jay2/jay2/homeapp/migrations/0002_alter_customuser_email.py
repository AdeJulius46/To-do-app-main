# Generated by Django 4.1.1 on 2022-09-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
