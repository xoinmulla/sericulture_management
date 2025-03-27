from django.urls import path
from . import views


urlpatterns = [
    path('add-farmer/', views.add_farmer, name='add_farmer'),
    path('market-trends/', views.market_trends, name='market_trends'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),


]
