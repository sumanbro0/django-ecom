# Generated by Django 4.1.4 on 2022-12-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cart_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]