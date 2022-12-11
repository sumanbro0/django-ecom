# Generated by Django 4.1.4 on 2022-12-09 08:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_cart_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_orderd', models.BooleanField(default=False)),
                ('is_delevered', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='accounts.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]