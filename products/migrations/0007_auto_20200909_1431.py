# Generated by Django 3.1 on 2020-09-09 14:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200908_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]