from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllDCView.as_view(), name='index'),
    path("register/", views.register_request, name="dc_"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("dc_form/", views.dc_form, name='dc_form'),
    path("devices/", views.AllDevicesView.as_view(), name='devices'),
    path("devices/<int:id>",views.dc_devices, name="dc_devices"),
    path("devices/<slug:slug>",views.DeviceDetailView.as_view(), name="device_detail"),
    path("devices/interfaces/", views.AllInterfacesView.as_view(), name="all_interfaces"),
    path("devices/interfaces/<slug:slug>",views.interfaces, name="interfaces"),
    path("device_form/<int:id>", views.device_form, name='device_form'),
    path("interface_form/<int:id>", views.interface_form, name='interface_form'),
    path("vix_clients/", views.VIX_Clients, name='vix_clients'),
    path("via_clients/", views.VIA_Clients, name='via_clients'),
    path("client_form/<int:id>", views.client_form, name='client_form'),
    path("all_client/", views.AllClientView.as_view(), name='client_list'),
    path("client_detail/?P<pk>\d+", views.ClientDetailView.as_view(), name='client_detail'),
    path("update/<int:id>", views.update, name = 'client_update'),
    path("update/updaterecord/<int:id>", views.updaterecord, name = 'updaterecord'),
]
