# Generated by Django 4.1.2 on 2022-10-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='component_name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Component Name'),
        ),
    ]