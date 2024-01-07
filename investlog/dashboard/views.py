from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'dashboard/index.html')