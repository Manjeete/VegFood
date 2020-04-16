from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopListView.as_view(), name='shop'),
    path('<int:pk>', views.ShopDetailView.as_view(), name='listing'),
]