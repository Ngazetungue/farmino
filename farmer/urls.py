from django.urls import path
from .views import (
    HomePageView,
    BillingListView,
    FarmerListView,
    BillingDetailView,
    BillingUpdateView,
    BillingDeleteView,
    FarmerApplyCreateView,
)

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
     path(
        "farmer-apply/", FarmerApplyCreateView.as_view(), name="farmer-apply"
    ),
    path("farmer-list/", FarmerListView.as_view(), name="farmer-list"),
    path("billing/", BillingListView.as_view(), name="billing"),
    path(
        "billing-update/<int:pk>/", BillingUpdateView.as_view(), name="billing-update"
    ),
    path("billing-detail/", BillingDetailView.as_view(), name="billing-detail"),
    path(
        "billing-delete/<int:pk>/", BillingDeleteView.as_view(), name="billing-delete"
    ),
]
