# Generated by Django 3.2.18 on 2023-03-21 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20230321_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='facility_name',
        ),
        migrations.AddField(
            model_name='receipts',
            name='facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts_facility', to='accounts.invoice'),
        ),
    ]
