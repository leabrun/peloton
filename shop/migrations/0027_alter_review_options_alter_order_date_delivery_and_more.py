# Generated by Django 4.1.7 on 2023-04-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_order_date_delivery_alter_order_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.CharField(max_length=20, null=True, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=70, verbose_name='Фамилия'),
        ),
    ]