from .models import Customer, Dog, Service, Appointment
from rest_framework import serializers



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','created', 'last_updated']



class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ['first_name', 'last_name', 'created', 'last_updated', 'customer']
        # depth = 1


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['name', 'description', 'created', 'last_updated']


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['start_date', 'end_date', 'created', 'last_updated', 'customer', 'dogs', 'services']