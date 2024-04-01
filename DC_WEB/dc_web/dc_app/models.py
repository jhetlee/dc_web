from django.db import models
from django.utils.text import slugify

# Create your models here.


class Data_center(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location


class Device(models.Model):
    hostname = models.CharField(max_length = 30)
    management_ip = models.CharField(max_length = 20)
    datacenter_location = models.ForeignKey(Data_center, on_delete=models.CASCADE, related_name='device')
    remote_access = models.CharField(max_length=30)
    device_os = models.CharField(max_length = 30)
    slug = models.SlugField(default="", blank = True ,null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.hostname)#format title to "harry-potter-1"
        super().save(*args, **kwargs)#save the slugify title to slug field

    def __str__(self):
        return self.hostname + "-" + self.management_ip


class Interface(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='interface')
    interface_id = models.CharField(max_length=200)
    interface_description = models.CharField(max_length=200)
    sfp_type = models.CharField(max_length=100, null=True, blank=True)
    sfp_brand = models.CharField(max_length=50, null=True, blank=True)
    sfp_sn = models.CharField(max_length=50, null=True, blank=True)
    has_client = models.BooleanField(null=True)

    def __str__(self):
        return self.interface_id + "-" + self.interface_description


#table for service
#VIX
#VIA
#DCI



class Client(models.Model):
    interface = models.OneToOneField(Interface, on_delete=models.CASCADE, related_name='client')
    sr_number = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    subscription = models.CharField(max_length=100)
    vlan = models.CharField(max_length=100, null=True, blank=True)
    bandwidth = models.CharField(max_length=100, null=True, blank=True)
    ip_block = models.CharField(max_length=100, null=True, blank=True)
#   client_status[for termination or not] = boolean
    # terminated

    def __str__(self):

        return str(self.pk) + " : " + self.client_name