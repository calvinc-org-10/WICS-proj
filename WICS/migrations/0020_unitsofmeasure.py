# Generated by Django 4.1.1 on 2023-03-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WICS", "0019_alter_wicspermissions_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnitsOfMeasure",
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
                ("UOM", models.CharField(max_length=50, unique=True)),
                ("UOMText", models.CharField(blank=True, default="", max_length=100)),
                (
                    "DimensionText",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("Multiplier1", models.FloatField(default=1.0)),
            ],
        ),
    ]
