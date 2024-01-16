# Generated by Django 5.0.1 on 2024-01-16 14:58

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Debt",
            fields=[
                (
                    "debt_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "creditor_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debts_as_creditor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "debtor_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debts_as_debtor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
