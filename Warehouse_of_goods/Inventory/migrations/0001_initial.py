# Generated by Django 4.2.6 on 2023-11-05 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("bank_details", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("volume", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Shelf",
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
                ("number", models.IntegerField()),
                ("storage_capacity", models.IntegerField()),
                ("height", models.DecimalField(decimal_places=2, max_digits=5)),
                ("width", models.DecimalField(decimal_places=2, max_digits=5)),
                ("length", models.DecimalField(decimal_places=2, max_digits=5)),
                ("max_load", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Inventory.room"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("height", models.DecimalField(decimal_places=2, max_digits=5)),
                ("width", models.DecimalField(decimal_places=2, max_digits=5)),
                ("length", models.DecimalField(decimal_places=2, max_digits=5)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=10)),
                ("arrival_date", models.DateField()),
                ("contract_number", models.CharField(max_length=100)),
                ("contract_end_date", models.DateField()),
                ("position", models.IntegerField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Inventory.client",
                    ),
                ),
                (
                    "shelf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Inventory.shelf",
                    ),
                ),
            ],
        ),
    ]