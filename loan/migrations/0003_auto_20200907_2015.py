# Generated by Django 3.1 on 2020-09-07 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20200907_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='request_number',
            new_name='order_number',
        ),
    ]
