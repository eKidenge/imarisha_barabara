# Generated by Django 4.2.7 on 2023-12-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FuelLog",
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
                ("ward", models.CharField(max_length=100)),
                ("subcounty", models.CharField(max_length=100)),
                ("equipment", models.CharField(max_length=100)),
                ("number_plate", models.CharField(max_length=20)),
                ("fuel_units", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "price_per_litre",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="FuelStation",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
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
                ("make", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
            ],
        ),
    ]
