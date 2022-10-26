from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import FarmerApplyForm
from .models import Billing, Client

# Create your views here


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "farmer/index.html"


"""
class FarmerApplyCreateView(CreateView):
    model = Client
    template_name = "farmer/pages/farmer_apply_create.html"
    success_url = reverse_lazy("login")
    fields = [
        "first_name",
        "last_name",
        "email",
        "town",
        "number_of_livestock",
    ]

"""


def farmer_apply_view(request):

    if request.method == "POST":
        form = FarmerApplyForm(request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        town = request.POST.get("town")
        number_of_livestock = request.POST.get("number_of_livestock") 

        if form.is_valid():
            farmer = Client()
            farmer.first_name = first_name
            farmer.last_name = last_name
            farmer.email = email
            farmer.town = town
            farmer.number_of_livestock = number_of_livestock

            farmer.save()
            return HttpResponseRedirect("")
    else:
        form = FarmerApplyForm()

    return render(request, "farmer/pages/farmer_apply_create.html", {"form": form})


class FarmerListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = "farmer_list"
    template_name = "farmer/pages/farmer_list.html"


class FarmerDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "farmer/pages/farmer_delete.html"
    success_url = reverse_lazy("farmer-list")


class BillingCreateView(LoginRequiredMixin, CreateView):
    model = Billing
    template_name = "farmer/pages/billing_create.html"
    success_url = reverse_lazy("billing")
    fields = [
        "title",
        "invoice_status",
        "note",
        "price_per_livestock",
        "discount_price",
        "client",
    ]


class BillingListView(LoginRequiredMixin, ListView):
    model = Billing
    context_object_name = "billing_list"
    template_name = "farmer/pages/billing.html"


class BillingDetailView(LoginRequiredMixin, DetailView):
    model = Billing
    context_object_name = "billing_detail"
    template_name = "formaer/pages/billing_detail.html"


class BillingUpdateView(LoginRequiredMixin, UpdateView):
    model = Billing
    template_name = "farmer/pages/billing_update.html"
    success_url = reverse_lazy("billing")
    fields = [
        "title",
        "invoice_status",
        "note",
        "price_per_livestock",
        "discount_price",
    ]


class BillingDeleteView(LoginRequiredMixin, DeleteView):
    model = Billing
    template_name = "farmer/pages/billing_delete.html"
    success_url = reverse_lazy("billing")
