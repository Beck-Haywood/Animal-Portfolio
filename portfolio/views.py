from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm


# Create your views here.
class PortfoliosView(ListView):
    """Renders a bunch of portfolios
    """
    model = Portfolio

    def get(self, request):
        """ Get a list of portfolios """
        portfolios = Portfolio.objects.all()
        return render(request, 'portfolios.html', {
        'portfolios' : portfolios
        })

class PortfolioView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Portfolio

    def get(self, request, slug):
        """ Returns a specific portfolio page by slug. """
        #page = self.get_queryset().get(slug__iexact=slug)
        page = Portfolio.objects.get(slug=slug)
        return render(request, 'portfolio.html', {
          'portfolio': page
        })
#class PortfolioCreateView(CreateView):
#    """Renders a bunch of portfolios
#    """
#    model = Portfolio
#    def post(request):
#        pass

#def upload(request):
#    context = {}
#    if request.method == 'POST':
#        uploaded_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(uploaded_file.name, uploaded_file)
#        context['url'] = fs.url(name)
#    return render(request, 'upload.html', context)
def upload(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PortfolioForm()
    return render(request, 'upload.html', { 
        'form': form 
        })
