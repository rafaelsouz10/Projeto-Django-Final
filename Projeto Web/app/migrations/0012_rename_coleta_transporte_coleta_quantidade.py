# Generated by Django 5.1.6 on 2025-02-28 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_transporte_data_envio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transporte',
            old_name='coleta',
            new_name='coleta_quantidade',
        ),
    ]
