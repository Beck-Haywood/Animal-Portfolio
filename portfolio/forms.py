from django import forms
from portfolio.models import Portfolio, Images

class PortfolioForm(forms.ModelForm):
    """ Render and process a form based on the Portfolio model. """
    title = forms.CharField(max_length=128)
    class Meta:
        model = Portfolio
        fields = '__all__'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )