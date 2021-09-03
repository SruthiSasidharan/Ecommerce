# Generated by Django 3.2.4 on 2021-08-24 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0003_remove_items_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecom.items')),
            ],
        ),
        migrations.CreateModel(
            name='Mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=130)),
                ('status', models.CharField(choices=[('cart', 'cart'), ('orderplaced', 'orderplaced')], default='cart', max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecom.items')),
            ],
        ),
    ]