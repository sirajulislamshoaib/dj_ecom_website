# Generated by Django 5.0.2 on 2024-03-07 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]
