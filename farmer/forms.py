from django import forms

from .models import Client, Billing


class FarmerApplyForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "email",
            "town",
            "number_of_livestock",
        ]


"""class CreateBillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = [
            "title",
            "invoice_status",
            "note",
            "price_per_livestock",
            "discount_price",
            "client",
        ]
"""