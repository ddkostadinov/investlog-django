from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InvestmentForm


class Overview(LoginRequiredMixin, View):

    def get(self, request):
        context = {'user': request.user}
        return render(request, 'dashboard/overview.html', context=context)
    
class Investments(LoginRequiredMixin, View):

    def get(self, request):
        context = {'user': request.user}
        return render(request, 'dashboard/investments.html', context=context)
    
class AddInvestment(LoginRequiredMixin, View):

    def get(self, request):
        form = InvestmentForm
        context = {'user': request.user}
        return render(request, 'dashboard/add-investment.html', {
            'context': context,
            'form': form
        })