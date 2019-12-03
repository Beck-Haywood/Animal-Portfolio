from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.list import ListView
#from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm


# Create your views here.
class PortfoliosView(ListView):
    """Renders a bunch of portfolios
    """
    def get(self, request):
        """ Get a list of portfolios """
        return render(request, 'portfolios.html')

'''def model_form_upload(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
    '''
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
"""    
class PortfolioCreateView(CreateView):
    template = 'new_portfolio.html'
    form_class = PortfolioForm
    success_url = '' 

    def get(self, request):
        form = PortfolioForm()
        return render(request, 'new_portfolio.html', {'form': form})
  
    def post(self, request):
        if request.method == 'POST':
            form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save()
            return HttpResponseRedirect(reverse_lazy('wiki-details-page', args = [portfolio.slug]))
        return render(request, 'new_portfolio.html', {'form': form})
        """