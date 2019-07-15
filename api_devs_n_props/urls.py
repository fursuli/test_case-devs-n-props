from django.urls import path

from api_devs_n_props.views import AllDevices, AllProperties, NewDevice, NewProperty

urlpatterns = [
    path('devices/', AllDevices.as_view()),
    path('properties/', AllProperties.as_view()),
    path('devices/<int:pk>/', AllDevices.as_view()),
    path('properties/<int:pk>/', AllProperties.as_view()),
    path('devices/new/', NewDevice.as_view()),
    path('properties/new/', NewProperty.as_view())
]
