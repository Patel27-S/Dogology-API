from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .serializers import AppointmentSerializer, CustomerSerializer, DogSerializer, ServiceSerializer
from .models import Appointment, Customer, Dog, Service

# Create your views here.
class CreateCustomer(CreateAPIView):
    model = Customer
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        try:
            instance = Customer.objects.get(email=email.lower())
        except:
            customer = Customer(first_name=first_name, last_name=last_name, email=email.lower())
            customer.save()
            return Response(
                            data={
                                f'{first_name} {last_name}':'Succesfully added to the database.'
                                }, 
                            status=status.HTTP_200_OK,
                            )
        if instance:
            return Response(
                            data={
                                'Error':'The customer is already existing. If it is a different customer\
                                    then enter another email for the customer as the mentioned is already\
                                        taken. '
                                         }, 
                            status=status.HTTP_400_BAD_REQUEST,
                            )


class ListCustomers(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        return Customer.objects.all()


class RetrieveUpdateDestroyCustomer(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    lookup_field = 'id'
    serializer_class = CustomerSerializer



# Create your views here.
class CreateDog(CreateAPIView):
    model = Dog
    serializer_class = DogSerializer

    def post(self, request, *args, **kwargs):

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        customer = request.data.get('customer')
        try:
            instance = Dog.objects.get(customer=customer, first_name= first_name, last_name= last_name)
        except:
            dog = Dog(first_name=first_name, last_name=last_name, customer=Customer.objects.get(id=customer))
            dog.save()
            return Response(
                            data={
                                f'{first_name} {last_name}':'Succesfully added to the database.'
                                }, 
                            status=status.HTTP_200_OK,
                            )

        return Response(
                        data={
                            'Error':'The dog is already added as a entry'
                            }, 
                        status=status.HTTP_400_BAD_REQUEST,
                        )

class ListDogs(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'customer']
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        return Dog.objects.all()

class RetrieveUpdateDestroyDog(RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    lookup_field = 'id'
    serializer_class = DogSerializer



class CreateService(CreateAPIView):
    model = Service
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):

        name = request.data.get('name')
        description = request.data.get('description')
        
        try:
            instance = Service.objects.get(name=name)
        except:
            service = Service(name=name, description=description)
            service.save()
            return Response(
                            data={
                                f'{name} service':'Succesfully created.'
                                }, 
                            status=status.HTTP_200_OK,
                            )
        if instance:
            return Response(
                            data={
                                'Error':'This service is already added. You might want \
                                    to update it but not re-create. '
                                }, 
                            status=status.HTTP_400_BAD_REQUEST,
                            )

class ListServices(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

    def get_queryset(self):
        return Service.objects.all()

class RetrieveUpdateDestroyService(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    lookup_field = 'name'
    serializer_class = ServiceSerializer


class CreateAppointment(CreateAPIView):
    model = Appointment
    serializer_class = AppointmentSerializer

    # def post(self, request, *args, **kwargs):

    #     name = request.data.get('name')
    #     description = request.data.get('description')
        
    #     try:
    #         instance = Service.objects.get(name=name)
    #     except:
    #         service = Service(name=name, description=description)
    #         service.save()
    #         return Response(
    #                         data={
    #                             f'{name} service':'Succesfully created.'
    #                             }, 
    #                         status=status.HTTP_200_OK,
    #                         )
    #     if instance:
    #         return Response(
    #                         data={
    #                             'Error':'This service is already added. You might want \
    #                                 to update it but not re-create. '
    #                             }, 
    #                         status=status.HTTP_400_BAD_REQUEST,
    #                         )

class ListAppointments(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['customer', 'created', 'end_date', 'services']
    search_fields = ['customer']

    def get_queryset(self):
        return Appointment.objects.all()

class RetrieveUpdateDestroyAppointment(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    lookup_field = 'id'
    serializer_class = AppointmentSerializer