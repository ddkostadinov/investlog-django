# dashboard/urls.py
from django.urls import path
from .views import Overview, Investments, AddInvestment, EditInvestment, DeleteInvestment

urlpatterns = [
    path('', Overview.as_view(), name='overview'),
    path('investments/', Investments.as_view(), name='investments'),
    path('add-investment/', AddInvestment.as_view(), name='add-investment'),
    path('edit-investment/<int:pk>', EditInvestment.as_view(), name='edit-investment'),
    path('delete-investment/<int:pk>', DeleteInvestment.as_view(), name='delete-investment'),
]