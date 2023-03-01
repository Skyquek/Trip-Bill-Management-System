# Generated by Django 4.1.6 on 2023-02-25 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0003_bill_individualspending_remove_payment_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="individualspending",
            name="title",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bill",
            name="note",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="individualspending",
            name="note",
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name="Debt",
        ),
    ]