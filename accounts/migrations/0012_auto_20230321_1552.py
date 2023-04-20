# Generated by Django 3.2.18 on 2023-03-21 12:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20230321_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='receipts',
            name='facility',
        ),
        migrations.AddField(
            model_name='bill',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invoice',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='receipts',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='receipts',
            name='payment_mode',
            field=models.CharField(choices=[('Mobile_Banking ', 'Mpesa'), ('Bank_Transaction', 'Cheque')], default='Mpesa', max_length=20),
        ),
        migrations.AddField(
            model_name='receipts',
            name='transaction',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.invoice'),
        ),
    ]
