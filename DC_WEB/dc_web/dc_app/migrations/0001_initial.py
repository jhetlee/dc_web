# Generated by Django 4.1 on 2023-11-07 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30)),
                ('management_ip', models.CharField(max_length=20)),
                ('remote_access', models.CharField(max_length=30)),
                ('device_os', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, default='')),
                ('datacenter_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='dc_app.data_center')),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_id', models.CharField(max_length=200)),
                ('interface_description', models.CharField(max_length=200)),
                ('sfp_type', models.CharField(blank=True, max_length=100, null=True)),
                ('sfp_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('sfp_sn', models.CharField(blank=True, max_length=50, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interface', to='dc_app.device')),
            ],
        ),
    ]
