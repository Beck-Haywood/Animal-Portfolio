from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.
class PortfoliosView(ListView):
    """Renders a bunch of portfolios
    """
    def get(self, request):
        """ Get a list of portfolios """
        return render(request, 'portfolios.html')