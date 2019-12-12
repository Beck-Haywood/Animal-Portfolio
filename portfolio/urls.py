from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from portfolio.views import PortfoliosView, PortfolioView, post #PortfolioCreateView
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', PortfoliosView.as_view() , name='portfolio-view-page'),
    path('upload/', views.post, name='upload'),
    path('<slug>/', PortfolioView.as_view(), name='portfolio'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)