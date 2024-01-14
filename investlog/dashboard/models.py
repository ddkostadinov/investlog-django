from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class InvestmentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    investment_type = models.CharField(max_length=50, choices=[('etf', 'ETF'), ('stock', 'Stock'), ('commodity', 'Commodity')], default=("stock", "Stock"))
    currency = models.CharField(max_length=3, choices=[('eur', 'EUR'), ('usd', 'USD'), ('gbp', 'GBP')], default=("usd", "USD"))
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('sold', 'Sold'), ('closed', 'Closed')], default=("active", "Active"))
    purchase_date = models.DateField(default=timezone.now)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dividends_interest = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    notes = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"