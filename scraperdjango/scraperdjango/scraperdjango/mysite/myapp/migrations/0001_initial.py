# Generated by Django 5.1.6 on 2025-02-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("address", models.CharField(blank=True, max_length=2000, null=True)),
                ("name", models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
