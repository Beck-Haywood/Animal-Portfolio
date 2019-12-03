from django.urls import path

from portfolio.views import PortfoliosView, PortfolioCreateView

app_name = 'portfolio'
urlpatterns = [
    path('', PortfoliosView.as_view() , name='portfolio-view-page'),
    path('create', PortfolioCreateView.as_view(), name='portfolio-create-page'),

]