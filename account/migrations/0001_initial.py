# Generated by Django 4.2.4 on 2023-08-18 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.UUID("7a50d2fe-15c4-4f75-a49a-4e6ea3b9a21a"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("contact", models.CharField(max_length=30)),
                ("message", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.UUID("7a50d2fe-15c4-4f75-a49a-4e6ea3b9a21a"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.UUID("7a50d2fe-15c4-4f75-a49a-4e6ea3b9a21a"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="profile")),
                ("contact_number", models.CharField(max_length=255)),
                ("is_email_verified", models.BooleanField(default=False)),
                (
                    "email_token",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Profile",
            },
        ),
    ]