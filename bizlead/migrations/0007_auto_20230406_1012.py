# Generated by Django 3.2.18 on 2023-04-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizlead', '0006_alter_conversion_demostatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='assessmentdate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='demodate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='expression',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='facility_license',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='krapin',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='report',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='reportdate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
