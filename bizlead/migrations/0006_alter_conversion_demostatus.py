# Generated by Django 3.2.18 on 2023-04-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizlead', '0005_auto_20230405_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='demostatus',
            field=models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING')], default='PENDING', max_length=30),
        ),
    ]
