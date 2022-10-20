from django import forms

from .models import Client


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
