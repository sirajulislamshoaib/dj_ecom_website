# Generated by Django 5.0.2 on 2024-03-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='required_amount_to_use_coupon',
            field=models.PositiveBigIntegerField(default=100),
            preserve_default=False,
        ),
    ]