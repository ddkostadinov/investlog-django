# dashboard/urls.py
from django.urls import path
from .views import OverviewView, InvestmentsView, AddInvestmentView, EditInvestmentView, DeleteInvestmentView, InvestmentGraphView

urlpatterns = [
    path('', OverviewView.as_view(), name='overview'),
    path('investments/', InvestmentsView.as_view(), name='investments'),
    path('add-investment/', AddInvestmentView.as_view(), name='add-investment'),
    path('edit-investment/<int:pk>', EditInvestmentView.as_view(), name='edit-investment'),
    path('delete-investment/<int:pk>', DeleteInvestmentView.as_view(), name='delete-investment'),
    path('graph-investment/', InvestmentGraphView.as_view(), name='graph-investment'),
    
]