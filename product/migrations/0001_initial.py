# Generated by Django 4.2.4 on 2023-08-18 07:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Destination",
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
                ("title", models.CharField(max_length=255)),
                ("grade", models.CharField(max_length=255)),
                ("fees", models.IntegerField()),
                ("meta_desc", models.TextField()),
                ("description", models.TextField()),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city",
                        to="product.city",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="country",
                        to="product.country",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DestinationImage",
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
                ("imgSrc", models.ImageField(upload_to="destination")),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="imgSrc",
                        to="product.destination",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="product.country",
            ),
        ),
    ]
