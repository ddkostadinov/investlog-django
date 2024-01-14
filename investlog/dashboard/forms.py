from django import forms
from .models import InvestmentModel

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = InvestmentModel
        fields = ['name', 'investment_type', 'currency', 'status', 'purchase_date', 'purchase_price', 'quantity', 'current_value', 'dividends_interest', 'notes']