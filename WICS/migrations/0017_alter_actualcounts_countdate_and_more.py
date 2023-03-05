# Generated by Django 4.1.1 on 2023-03-04 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WICS", "0016_alter_whseparttypes_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actualcounts",
            name="CountDate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="countschedule",
            name="CountDate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="sap_sohrecs",
            name="uploaded_at",
            field=models.DateField(),
        ),
        migrations.AddConstraint(
            model_name="countschedule",
            constraint=models.UniqueConstraint(
                models.F("org"),
                models.F("CountDate"),
                models.F("Material"),
                name="CSchdUNQ_org_CDate_Material",
            ),
        ),
        migrations.AddConstraint(
            model_name="materiallist",
            constraint=models.UniqueConstraint(
                models.F("org"), models.F("Material"), name="MatlListUNQ_org_Material"
            ),
        ),
        migrations.AddConstraint(
            model_name="whseparttypes",
            constraint=models.UniqueConstraint(
                models.F("org"), models.F("WhsePartType"), name="PTypeUNQ_org_PType"
            ),
        ),
        migrations.AddConstraint(
            model_name="whseparttypes",
            constraint=models.UniqueConstraint(
                models.F("org"),
                models.F("PartTypePriority"),
                name="PTypeUNQ_org_PTypePrio",
            ),
        ),
    ]
