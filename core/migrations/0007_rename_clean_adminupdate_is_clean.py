# Generated by Django 4.1.2 on 2023-01-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_adminupdate_clean_alter_adminupdate_manual'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminupdate',
            old_name='clean',
            new_name='is_clean',
        ),
    ]