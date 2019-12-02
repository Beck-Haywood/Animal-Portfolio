from django.urls import path

from portfolio.views import PortfoliosView

app_name = 'portfolio'
urlpatterns = [
    path('', PortfoliosView.as_view() , name='portfolio-view-page'),
]