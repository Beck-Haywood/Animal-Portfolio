from django import forms
from portfolio.models import Portfolio

class PortfolioForm(forms.ModelForm):
    """ Render and process a form based on the Portfolio model. """
    class Meta:
        model = Portfolio
        fields = '__all__'

