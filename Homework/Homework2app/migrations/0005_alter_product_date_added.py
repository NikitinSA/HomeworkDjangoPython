# Generated by Django 4.2.4 on 2023-09-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework2app', '0004_product_date_added_product_description_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]