from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

from portfolio.models import Portfolio
from portfolio.models import Images
from portfolio.forms import PortfolioForm
from portfolio.forms import ImageForm

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def post(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PortfolioForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(portfolio=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(f'ERRORS: POSTFORm:{postForm.errors}, FORmSET:{formset.errors}')
    else:
        postForm = PortfolioForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'upload.html',
                  {'postForm': postForm, 'formset': formset})

class PortfoliosView(ListView):
    """Renders a bunch of portfolios
    """
    model = Portfolio

    def get(self, request):
        """ Get a list of portfolios """
        portfolios = Portfolio.objects.all()
        images = Images.objects.filter(portfolio=portfolios)
        return render(request, 'portfolios.html', {
        'portfolios' : portfolios, 'images': images
        })

class PortfolioView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Portfolio

    def get(self, request, slug):
        """ Returns a specific portfolio page by slug. """
        #page = self.get_queryset().get(slug__iexact=slug)
        page = Portfolio.objects.get(slug=slug)
        images = Images.objects.filter(portfolio=page)
        return render(request, 'portfolio.html', {
          'portfolio': page, 'images': images
        })

# def upload(request):
#     if request.method == 'POST':
#         form = PortfolioForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = PortfolioForm()
#     return render(request, 'upload.html', { 
#         'form': form 
#         })
