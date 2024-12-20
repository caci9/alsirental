# Generated by Django 5.1.1 on 2024-10-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qera', '0007_reservation_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='full_name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]
