# Generated by Django 3.2.4 on 2021-08-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='isbn',
        ),
    ]