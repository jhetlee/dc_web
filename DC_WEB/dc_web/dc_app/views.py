from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Device, Interface, Data_center, Client
from .forms import DatacenterForm, DeviceForm, InterfaceForm, NewUserForm, ClientForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, View, UpdateView
from django.urls import reverse_lazy
# Create your views here.





#@login_required(login_url='/dc_app/login/')
class AllDCView(ListView):
    template_name = "dc_app/index.html"
    model = Data_center
    context_object_name = "datacenters"

"""
def index(request):
    all_dc = Data_center.objects.all()
    return render(request, "dc_app/index.html",
                  {
                      "datacenters":all_dc,
                  })
"""


def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return HttpResponseRedirect('/dc_app/login/')
        messages.error(request, "Unsuccessful registration. Invalid Information")
        form = NewUserForm()
        return render(request,"dc_app/register.html", {
            "register_form":form
        })
    return render(request, "dc_app/register.html", {
        "form":NewUserForm()
    })


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/dc_app')
            else:
                messages.error(request, f"Invalid Username or Password")
        else:
            messages.error(request, f"Invalid Username or Password")
    form = AuthenticationForm()
    return render(request, 'dc_app/login.html', {
        "login_form":form
    })

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logout!")
    return HttpResponseRedirect('/dc_app/login/')

#@login_required(login_url='/dc_app/login/')
class AllDevicesView(ListView):
    template_name = "dc_app/devices.html"
    model = Device
    context_object_name = "devices"

"""    
def devices(request):
    all_devices = Device.objects.all()
    return render(request, "dc_app/devices.html", {
        "devices":all_devices
    })
"""


#@login_required(login_url='/dc_app/login/')
def interfaces(request, slug):
    device_identified_interface = Device.objects.get(slug=slug)
    device_interfaces = device_identified_interface.interface.all()
    return render(request, "dc_app/device_interface.html", {
        "device_interfaces": device_interfaces,
        "device_identified_interface":device_identified_interface
    })


#@login_required(login_url='/dc_app/login/')
class AllInterfacesView(ListView):
    template_name = "dc_app/all_interfaces.html"
    model = Interface
    context_object_name = "all_interfaces"

"""
def all_interfaces(request):
    all_interfaces = Interface.objects.all()
    return render(request, "dc_app/all_interfaces.html", {
        "all_interfaces":all_interfaces
    })
"""

#@login_required(login_url='/dc_app/login/')
class DeviceDetailView(DetailView):
    template_name = "dc_app/device_detail.html"
    model = Device

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["device"] = self.object
        return context

"""
def device_detail(request, slug):
    #identified_device = next(interf for interf in all_devices if interf['slug']==slug)
    identified_device = Device.objects.get(slug=slug)
    return render(request, "dc_app/device_detail.html", {
        "device":identified_device
    })
"""


#@login_required(login_url='/dc_app/login/')
def dc_devices(request, id):
    dc_location = Data_center.objects.get(id=id)
    identified_dc_devices =  Device.objects.filter(datacenter_location = id)
    return render(request, "dc_app/dc_devices.html", {
        "identified_dc_devices":identified_dc_devices,
        "dc_location":dc_location
    })

#@login_required(login_url='/dc_app/login/')
def dc_form(request):
    if request.method == "POST":
        form = DatacenterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dc_app')
    else:
        form = DatacenterForm
    return render(request, "dc_app/device_form.html", {
        "form" : form
    })

#@login_required(login_url='/dc_app/login/')
def device_form(request, id):
    dc = Data_center.objects.get(id=id)
    print(dc)
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = Device(hostname=form.cleaned_data['hostname'],
                            management_ip=form.cleaned_data['management_ip'],
                            datacenter_location=dc,
                            remote_access=form.cleaned_data['remote_access'],
                            device_os=form.cleaned_data['device_os']
                            )
            device_check = Device.objects.filter(management_ip=form.cleaned_data['management_ip']).exists()
            device_check2 = Device.objects.filter(hostname=form.cleaned_data['hostname']).exists()
            if device_check or device_check2:
                return render(request, "dc_app/deviceForm.html", {
                   "device_exist": True,
                    "form":form
                })
            else:
                device.save()
                return HttpResponseRedirect(f"/dc_app/devices/{id}")
    else:
        form = DeviceForm()
    return render(request, "dc_app/deviceForm.html", {
        "form":form
    })

#@login_required(login_url='/dc_app/login/')
def interface_form(request, id):
    device = Device.objects.get(id=id)
    if request.method == "POST":
        form = InterfaceForm(request.POST)
        if form.is_valid():
            interface = Interface(
                device=device,
                interface_id=form.cleaned_data['interface_id'],
                interface_description=form.cleaned_data['interface_description'],
                sfp_type=form.cleaned_data['sfp_type'],
                sfp_brand=form.cleaned_data['sfp_brand'],
                sfp_sn=form.cleaned_data['sfp_sn']
            )

            interface.save()
            return HttpResponseRedirect(f"/dc_app/devices/interfaces/{device.slug}")
    else:
        form = InterfaceForm()
    return render(request, "dc_app/interfaceForm.html", {
            "form": form
        })

def VIX_Clients(request):
    all_vix_client = Client.objects.filter(id=1)

    print()
    return render(request, "dc_app/VIX_Clients.html", {
        "all_vix_clients":all_vix_client
    })

def VIA_Clients(request):
    all_via_client = Client.objects.filter(id=2)
    return render(request, "dc_app/VIA_Clients.html", {
        "all_via_client":all_via_client
    })

class AllClientView(ListView):
    template_name = "dc_app/all_client.html"
    model = Client
    context_object_name = "all_client"
"""
def client_list(request):
    all_client = Client.objects.all()
    return render(request, "dc_app/all_client.html", {
        "all_client":all_client
    })
"""

def client_form(request, id):

    interface = Interface.objects.get(id=id)
    client_exist = interface.has_client
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = Client(
                interface = interface,
                sr_number = form.cleaned_data['sr_number'],
                client_name = form.cleaned_data['client_name'],
                subscription = form.cleaned_data['subscription'],
                vlan = form.cleaned_data['VLAN'],
                bandwidth = form.cleaned_data['bandwidth'],
                ip_block = form.cleaned_data['ip_block']

            )
            client_check = Client.objects.filter(sr_number=form.cleaned_data['sr_number']).exists()
            VLAN_check = Client.objects.filter(vlan=form.cleaned_data['VLAN']).exists()
            ip_block_check = Client.objects.filter(ip_block=form.cleaned_data['ip_block']).exists()


            if client_check or VLAN_check or ip_block_check or client_exist:

                return render(request, "dc_app/clientForm.html", {
                    "form": form,
                    "client_exist": client_exist
                })
            else:

                client.save()
                interface.has_client = "True"
                interface.save()
                return HttpResponseRedirect(f"/dc_app/devices/")

    else:
        form = ClientForm()
    return render(request, "dc_app/clientForm.html", {
        "form": form,
        "client_exist":client_exist
    })

"""
def client_detail(request, id):
    interface = Interface.objects.get(id=id)
    return render(request,"dc_app/client_detail.html",{
        "interface":interface
    })
"""
class ClientDetailView(DetailView):
    template_name = "dc_app/client_detail.html"
    model = Interface

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["interface"] = self.object
        return context


class ClientUpdateView(UpdateView):
    fields = (
        "sr_number",
        "client_name",
        "subscription",
        "vlan",
        "bandwidth",
        "ip_block"
    )
    model = Client
    success_url = '/dc_app/devices/'

def update(request, id):
    mymember = Client.objects.get(id=id)
    context = {
        "mymember":mymember
    }
    return render(request, "dc_app/update.html", context)

def updaterecord(request,id):
    sr_number = request.POST['sr_number']
    client_name = request.POST['client_name']
    subscription = request.POST['subscription']
    vlan = request.POST['vlan']
    bandwidth = request.POST['bandwidth']
    ip_block = request.POST['ip_block']

    client = Client.objects.get(id=id)
    client.sr_number = sr_number
    client.client_name = client_name
    client.subscription = subscription
    client.bandwidth = bandwidth
    client.vlan = vlan
    client.ip_block = ip_block

    client.save()
    return HttpResponseRedirect(f"/dc_app/devices/")