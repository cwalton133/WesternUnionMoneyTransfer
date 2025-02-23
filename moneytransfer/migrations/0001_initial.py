# Generated by Django 5.1.6 on 2025-02-07 22:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Agent",
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
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("contact_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Receiver",
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
                ("full_name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("nationality", models.CharField(max_length=100)),
                ("government_issued_id", models.CharField(max_length=255)),
                ("contact_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Sender",
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
                ("address", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("nationality", models.CharField(max_length=100)),
                ("government_issued_id", models.CharField(max_length=255)),
                ("contact_number", models.CharField(max_length=15)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("currency", models.CharField(max_length=3)),
                ("purpose", models.TextField()),
                ("mtcn", models.CharField(max_length=15, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Completed", "Completed"),
                            ("Cancelled", "Cancelled"),
                            ("Failed", "Failed"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moneytransfer.agent",
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moneytransfer.receiver",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="moneytransfer.sender",
                    ),
                ),
            ],
        ),
    ]
