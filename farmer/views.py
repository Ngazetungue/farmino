from multiprocessing.connection import Client
from pyexpat import model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, Billing
from django.urls import reverse_lazy

# Create your views here.


class HomePageView(TemplateView):
    template_name = "farmer/index.html"

class FarmerApplyCreateView(CreateView):
    model = Client
    template_name = "farmer/pages/farmer_apply_create.html"
    success_url = reverse_lazy("login")
    fields = [
        'first_name',
'last_name',
'email',
'town',
'number_of_livestock',
    
    ]

class FarmerListView(ListView):
    model = Client
    context_object_name = "farmer_list"
    template_name = "farmer/pages/tables.html"

class BillingCreateView(CreateView):
    model = Billing
    template_name = "farmer/pages/billing_create.html"
    success_url = reverse_lazy("billing")
    fields = [
        "uniqueId",
        "note",
        "invoice_status",
    ]

class BillingListView(ListView):
    model = Billing
    context_object_name = "billing_list"
    template_name = "farmer/pages/billing.html"


class BillingDetailView(DetailView):
    model = Billing
    context_object_name = "billing_detail"
    template_name = "formaer/pages/billing_detail.html"


class BillingUpdateView(UpdateView):
    model = Billing
    template_name = "farmer/pages/billing_update.html"
    success_url = reverse_lazy("billing")
    fields = [
        "uniqueId",
        "note",
        "invoice_status",
    ]


class BillingDeleteView(DeleteView):
    model = Billing
    template_name = "farmer/pages/billing_delete.html"
    success_url = reverse_lazy("billing")
