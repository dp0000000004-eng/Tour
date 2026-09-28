from django import forms
from .models import TourForm


class TourFormForm(forms.ModelForm):

    class Meta:
        model = TourForm
        fields = ["name", "branch", "contact_no", "email"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your name",
                "class": "input"
            }),

            "branch": forms.Select(attrs={
                "class": "input"
            }),

            "contact_no": forms.NumberInput(attrs={
                "placeholder": "Enter contact number",
                "class": "input"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email",
                "class": "input"
            }),
        }