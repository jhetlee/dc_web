# Generated by Django 3.2 on 2023-11-08 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_number', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('subscription', models.CharField(max_length=100)),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='dc_app.interface')),
            ],
        ),
        migrations.CreateModel(
            name='Client_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_block', models.CharField(max_length=100)),
                ('bandwidth', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_detail', to='dc_app.client')),
            ],
        ),
    ]
