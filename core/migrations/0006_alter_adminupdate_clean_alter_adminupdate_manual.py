# Generated by Django 4.1.2 on 2023-01-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_adminupdate_alter_turbidityrecord_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminupdate',
            name='clean',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adminupdate',
            name='manual',
            field=models.BooleanField(default=False),
        ),
    ]
