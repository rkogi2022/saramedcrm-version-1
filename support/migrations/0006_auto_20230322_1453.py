# Generated by Django 3.2.18 on 2023-03-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_auto_20230322_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='module',
            field=models.CharField(choices=[('Patient_Register', 'PATIENT REGISTER'), ('Nurse', 'NURSE'), ('Doctor', 'DOCTOR'), ('Laboratory', 'LABORATORY'), ('Radiography', 'RADIOGRAPHY'), ('Inpatient', 'INPATIENT'), ('Pharmacy', 'PHARMACY'), ('Cashier', 'CASHIER'), ('Inventory', 'INVENTORY'), ('Finance', 'FINANCE'), ('Human_Resource', 'HUMAN RESOURCE'), ('System_Admin', 'SYSTEM ADMIN')], default='PATIENT REGISTER', max_length=30),
        ),
        migrations.AlterField(
            model_name='support',
            name='status',
            field=models.CharField(choices=[('Incomplete ', 'PENDING'), ('Complete', 'DONE')], default='DONE', max_length=20),
        ),
    ]
