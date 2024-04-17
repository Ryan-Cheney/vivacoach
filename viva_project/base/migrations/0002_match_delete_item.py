# Generated by Django 5.0.4 on 2024-04-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("points", models.JSONField()),
                ("matchOutcome", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Item",
        ),
    ]