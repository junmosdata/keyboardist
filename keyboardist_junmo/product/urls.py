from django.urls import path
from product import views

from product.models import *

app_name = 'product'

urlpatterns = [
    path('', views.ProductLV.as_view(), name='index'),
    path('product', views.ProductLV.as_view(), name='product_list'),
    path('product/<int:pk>', views.ProductDV.as_view(), name='product_detail'),
    
    path('search/', views.SearchFV.as_view(), name='search'),
    
    path('add/', views.PostCreateView.as_view(), name='add'),
    path('change/', views.PostChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]