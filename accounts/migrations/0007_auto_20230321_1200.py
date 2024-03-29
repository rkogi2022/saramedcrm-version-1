# Generated by Django 3.2.18 on 2023-03-21 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_invoice_invoice_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_invoice',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amt_paid', models.PositiveIntegerField(default=0)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.bill')),
                ('invoice', models.ForeignKey(db_column='invoice', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.invoice', to_field='total_invoice')),
            ],
        ),
    ]
