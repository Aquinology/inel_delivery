# Generated by Django 3.0.11 on 2020-12-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_applicationform_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryman',
            name='name',
            field=models.CharField(default='Елена', max_length=255, verbose_name='ИФО'),
            preserve_default=False,
        ),
    ]
