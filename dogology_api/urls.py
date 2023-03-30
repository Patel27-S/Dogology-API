from django.urls import path

from dogology_api.api_views import CreateAppointment, CreateCustomer, CreateDog, CreateService, ListAppointments, ListCustomers, ListDogs, ListServices, RetrieveUpdateDestroyAppointment, RetrieveUpdateDestroyCustomer, RetrieveUpdateDestroyDog, RetrieveUpdateDestroyService

app_name = 'dogology_api'

urlpatterns = [
    path('create_customer/', CreateCustomer.as_view(), name='create_customer'),
    path('list_customers/', ListCustomers.as_view(), name='list_customers'),
    path('rud_customer/<int:id>', RetrieveUpdateDestroyCustomer.as_view(), name='update_customer'),

    path('create_dog/', CreateDog.as_view(), name='create_dog'),
    path('list_dogs/', ListDogs.as_view(), name='list_dogs'),
    path('rud_dog/<int:id>', RetrieveUpdateDestroyDog.as_view(), name='update_dog'),

    path('create_service/', CreateService.as_view(), name='create_service'),
    path('list_services/', ListServices.as_view(), name='list_services'),
    path('rud_service/<str:name>', RetrieveUpdateDestroyService.as_view(), name='update_service'),

    path('create_appointment/', CreateAppointment.as_view(), name='create_appointment'),
    path('list_appointments/', ListAppointments.as_view(), name='list_appointments'),
    path('rud_appointment/<int:id>', RetrieveUpdateDestroyAppointment.as_view(), name='update_appointment'),
]