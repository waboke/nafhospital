# Generated by Django 4.0.2 on 2022-06-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0005_rename_personal_info_address_patient_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Christianity'), ('M', 'Islam'), ('O', 'Others')], max_length=1, null=True),
        ),
    ]