# Generated by Django 3.2.18 on 2023-03-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_bimonthly'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bimonthly',
            old_name='facility',
            new_name='facility_name',
        ),
        migrations.RenameField(
            model_name='bimonthly',
            old_name='feedback',
            new_name='feedback_given',
        ),
    ]
