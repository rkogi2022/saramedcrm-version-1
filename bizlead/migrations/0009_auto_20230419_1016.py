# Generated by Django 3.2.18 on 2023-04-19 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bizlead', '0008_auto_20230419_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteassessment',
            name='site_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bizlead.bizlead'),
        ),
        migrations.AddField(
            model_name='supportingdoc',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bizlead.bizlead'),
        ),
    ]