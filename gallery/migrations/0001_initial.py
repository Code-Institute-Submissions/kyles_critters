# Generated by Django 3.1 on 2020-09-08 10:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_auto_20200830_1303'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_number', models.CharField(editable=False, max_length=32)),
                ('critter_name', models.CharField(max_length=50)),
                ('critter_info', models.TextField(blank=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('critter_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='profiles.userprofile')),
            ],
        ),
    ]
