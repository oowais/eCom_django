# Generated by Django 3.2.9 on 2021-11-13 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='products',
            new_name='product',
        ),
    ]
