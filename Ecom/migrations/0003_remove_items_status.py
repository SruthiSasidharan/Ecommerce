# Generated by Django 3.2.4 on 2021-08-24 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0002_remove_items_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='status',
        ),
    ]
