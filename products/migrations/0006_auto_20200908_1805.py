# Generated by Django 3.1 on 2020-09-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200830_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='ready_to_loan',
            field=models.BooleanField(default=False),
        ),
    ]
