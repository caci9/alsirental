# Generated by Django 5.1.2 on 2024-11-10 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qera', '0011_alter_reservation_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='customer',
            new_name='user',
        ),
    ]
