# Generated by Django 3.2.18 on 2023-04-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0012_alter_support_completiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='problem',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='support',
            name='solution',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
