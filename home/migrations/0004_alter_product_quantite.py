# Generated by Django 4.2.4 on 2023-08-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_remove_product_name_alter_product_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Quantite",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]