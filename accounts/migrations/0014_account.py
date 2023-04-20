# Generated by Django 3.2.18 on 2023-03-22 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_rename_transaction_receipts_transaction_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=70)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('facility_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.invoice')),
            ],
        ),
    ]
