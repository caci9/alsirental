# Generated by Django 5.1.1 on 2024-09-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qera', '0004_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
