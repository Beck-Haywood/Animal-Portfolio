from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from portfolio.views import PortfoliosView, upload, PortfolioView #PortfolioCreateView
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', PortfoliosView.as_view() , name='portfolio-view-page'),
    path('upload/', views.upload, name='upload'),
    path('<slug>/', PortfolioView.as_view(), name='portfolio'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)