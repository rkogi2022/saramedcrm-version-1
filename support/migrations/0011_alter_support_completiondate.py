# Generated by Django 3.2.18 on 2023-03-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0010_auto_20230327_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='completiondate',
            field=models.DateField(blank=True),
        ),
    ]