# Generated by Django 4.2.4 on 2023-08-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_info_product_date_rename_name_product_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="Name",
        ),
        migrations.AlterField(
            model_name="product",
            name="Date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="Quantite",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="UPC",
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
