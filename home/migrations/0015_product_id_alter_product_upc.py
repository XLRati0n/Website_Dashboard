# Generated by Django 4.2.4 on 2023-08-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_rename_qutite_product_quantite"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="id",
            field=models.AutoField(
               primary_key=True
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="UPC",
            field=models.CharField(max_length=200),
        ),
    ]
