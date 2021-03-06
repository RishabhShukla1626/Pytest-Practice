# Generated by Django 3.2 on 2021-04-17 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Companies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Layoffs", "Layoff"),
                            ("Hiring Freeze", "Hiring Freeze"),
                            ("Hiring", "Hiring"),
                        ],
                        default="Hiring",
                        max_length=30,
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("application_notes", models.URLField(blank=True, max_length=100)),
            ],
        ),
    ]
