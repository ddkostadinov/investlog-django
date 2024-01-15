from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from .forms import InvestmentForm
from .models import InvestmentModel


class Overview(LoginRequiredMixin, View):

    def get(self, request):
        context = {'user': request.user}
        return render(request, 'dashboard/overview.html', context=context)
    
class Investments(LoginRequiredMixin, View):
    model = InvestmentModel
    template_name = 'investments.html'
    
    def get(self, request):
        investments = InvestmentModel.objects.filter(user=self.request.user)
        context = {'user': request.user,
                   'investments': investments}
        return render(request, 'dashboard/investments.html', context=context)
    
class AddInvestment(LoginRequiredMixin, CreateView):
    model = InvestmentModel
    form_class = InvestmentForm
    template_name = 'dashboard/add-investment.html'
    success_url = reverse_lazy('investments')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request):
        form = InvestmentForm
        context = {'user': request.user}
        return render(request, 'dashboard/add-investment.html', {
            'context': context,
            'form': form
        })