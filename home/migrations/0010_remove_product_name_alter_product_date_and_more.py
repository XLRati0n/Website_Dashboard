# Generated by Django 4.2.4 on 2023-08-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_remove_product_name_product_quantite_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="Name",
        ),
        migrations.AlterField(
            model_name="product",
            name="Date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="Quantite",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="UPC",
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]