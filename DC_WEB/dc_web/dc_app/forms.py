from django import forms
from .models import Data_center, Device, Interface, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DatacenterForm(forms.ModelForm):
    class Meta:
        model = Data_center
        fields = '__all__'
        labels = {
            "location":"location"
        }

class DeviceForm(forms.Form):
    hostname = forms.CharField(
        label="Hostname",
        max_length=30,
        error_messages={
            "required":'Hostname must not be empty',
            "max_length":"Please enter shorter hostname"
        }
    )
    management_ip = forms.CharField(
        label="Management IP",
        max_length=20,
        error_messages={
            "required":"Management IP must not be empty",
            "max_length":"Please enter shorter Management IP"
        }
    )
    """
    datacenter_location = forms.CharField(
        label="Data Center Location",
        max_length=30,
        error_messages={
            "required":"Data Center Location must not be empty",
            "max_length":"Please enter shorter Data Center Location"
        }
    )
    """
    remote_access = forms.CharField(
        label="Remote Access",
        max_length=20,
        error_messages={
            "required":"Remote Access must not be empty",
            "max_length":"Please enter shorter Remote Access type"
        }
    )
    device_os = forms.CharField(
        label="OS",
        max_length=20,
        error_messages={
            "required": "OS must not be empty",
            "max_length": "Please enter shorter OS type"
        }
    )
    """
    slug = forms.CharField(
        label="Slug",
        max_length=20,
        error_messages={
            "required": "Slug must not be empty",
            "max_length": "Please enter shorter Slug type"
        }
    )
"""



class InterfaceForm(forms.Form):
    interface_id = forms.CharField(
        label="Interface ID",
        max_length=20,
        error_messages={
            "required": "Interface ID must not be empty",
            "max_length": "Please enter shorter interface_id type"
        }
    )
    interface_description = forms.CharField(
        label="Interface Descsription",
        max_length=100,
        error_messages={
            "required": "Description must not be empty",
            "max_length": "Please enter shorter Description type"
        }
    )
    sfp_type = forms.CharField(
        label="SFP TYPE",
        max_length=20,
        error_messages={
            "required": "sfp_type must not be empty",
            "max_length": "Please enter shorter sfp_type type"
        }
    )
    sfp_brand = forms.CharField(
        label="SFP BRAND",
        max_length=20,
        error_messages={
            "required": "sfp_brand must not be empty",
            "max_length": "Please enter shorter sfp_brand type"
        }
    )
    sfp_sn = forms.CharField(
        label="SFP SN",
        max_length=20,
        error_messages={
            "required": "sfp_sn must not be empty",
            "max_length": "Please enter shorter sfp_sn type"
        }
    )


class ClientForm(forms.Form):
    sr_number = forms.CharField(
        label="SR Number",
        max_length=20,
        error_messages={
            "required": "SR number must not be empty",
            "max_length": "Please enter shorter SR Number type"
        })

    client_name = forms.CharField(
        label="Client",
        max_length=20,
        error_messages={
            "required": "Client must not be empty",
            "max_length": "Please enter shorter Client type"
        })

    subscription = forms.CharField(
        label="Subscription",
        max_length=20,
        error_messages={
            "required": "Subscription must not be empty",
            "max_length": "Please enter shorter Subscription type"
        })

    VLAN = forms.CharField(
        label="VLAN ID",
        max_length=20,
        error_messages={
            "required": "VLAN ID must not be empty",
            "max_length": "Please enter shorter VLAN ID type"
        })

    bandwidth = forms.CharField(
        label="Bandwidth",
        max_length=20,
        error_messages={
            "required": "Bandwidth must not be empty",
            "max_length": "Please enter shorter Bandwidth type"
        })

    ip_block = forms.CharField(
        label="IP Block",
        max_length=20,
        error_messages={
            "required": "IP Block must not be empty",
            "max_length": "Please enter shorter IP Block type"
        })

