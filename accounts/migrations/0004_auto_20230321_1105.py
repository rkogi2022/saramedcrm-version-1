# Generated by Django 3.2.18 on 2023-03-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_invoice_receipts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='receipts',
            name='invoice',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Receipts',
        ),
    ]
