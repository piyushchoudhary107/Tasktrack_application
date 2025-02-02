# Generated by Django 5.1.4 on 2025-01-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="category",
            field=models.CharField(
                choices=[
                    ("Work", "Work"),
                    ("Personal", "Personal"),
                    ("Urgent", "Urgent"),
                    ("Other", "Other"),
                ],
                default="other",
                max_length=50,
            ),
        ),
    ]
