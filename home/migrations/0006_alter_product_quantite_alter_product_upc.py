# Generated by Django 4.2.4 on 2023-08-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_product_upc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Quantite",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="UPC",
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]