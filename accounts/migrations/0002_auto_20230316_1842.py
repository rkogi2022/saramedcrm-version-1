# Generated by Django 3.2.18 on 2023-03-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='tax',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='total_cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]