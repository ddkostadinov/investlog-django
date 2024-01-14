# dashboard/urls.py
from django.urls import path
from .views import Overview, Investments, AddInvestment

urlpatterns = [
    path('', Overview.as_view(), name='overview'),
    path('investments/', Investments.as_view(), name='investments'),
    path('add-investment/', AddInvestment.as_view(), name='add-investment'),
]