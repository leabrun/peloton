# Generated by Django 4.1.6 on 2023-03-02 15:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_orderline_email_remove_product_cast_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ves',
            field=models.IntegerField(blank=True, help_text='гр.', null=True, verbose_name='Вес'),
        ),
    ]
