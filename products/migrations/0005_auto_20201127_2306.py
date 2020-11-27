# Generated by Django 3.0.11 on 2020-11-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_orderproduct_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='ИФО'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Номер телефона'),
        ),
    ]
