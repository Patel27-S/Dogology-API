from django.db import models

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.http import urlencode
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime


class Customer(models.Model):

    # Fields
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ("created",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Dog(models.Model):
    # Fields
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationships
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'
        ordering = ("first_name",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Service(models.Model):
    # Fields
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Metadata
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ("name",)

    # Model Functions
    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    # Code Part 1.1 here
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationships :
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dogs = models.ManyToManyField(Dog)
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ("start_date",)

    def __str__(self):
        # return str(self.customer.first_name + " " + self.customer.last_name +
        #            (self.start_date))
        return f"{self.customer.first_name} {self.customer.last_name} ({self.start_date})"


#  return f"self.first_name self.last_name ({self.start_date})"
# # return str(self.firs)
# datetime.strptime({self.start_date}, "%m/%d%Y/T%H:%M:%S.%f%z")
