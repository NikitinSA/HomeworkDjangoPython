# Generated by Django 4.2.4 on 2023-08-31 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework2app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_descripsion',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_quantiti',
            new_name='product_quantity',
        ),
    ]