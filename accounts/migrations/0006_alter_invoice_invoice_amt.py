# Generated by Django 3.2.18 on 2023-03-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_amt',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]