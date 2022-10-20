from django.urls import path

from .views import (
    BillingDeleteView,
    BillingDetailView,
    BillingListView,
    BillingUpdateView,
    FarmerListView,
    BillingCreateView,
    FarmerDeleteView,
    HomePageView,
)
from . import views

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("farmer-apply/", views.farmer_apply_view, name="farmer-apply"),
    path(
        "farmer-delete/<int:pk>/delete/",
        FarmerDeleteView.as_view(),
        name="farmer-delete",
    ),
    path("farmer-list/", FarmerListView.as_view(), name="farmer-list"),
    path("billing-create/", BillingCreateView.as_view(), name="billing-create"),
    path("billing/", BillingListView.as_view(), name="billing"),
    path(
        "billing-update/<int:pk>/", BillingUpdateView.as_view(), name="billing-update"
    ),
    path("billing-detail/", BillingDetailView.as_view(), name="billing-detail"),
    path(
        "billing-delete/<int:pk>/", BillingDeleteView.as_view(), name="billing-delete"
    ),
]
