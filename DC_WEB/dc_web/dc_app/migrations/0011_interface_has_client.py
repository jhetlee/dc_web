# Generated by Django 3.2 on 2024-02-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_app', '0010_alter_client_interface'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='has_client',
            field=models.BooleanField(null=True),
        ),
    ]
