# Generated by Django 3.2.18 on 2023-03-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_account_no_of_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='no_of_days',
            field=models.DurationField(blank=True),
        ),
    ]
