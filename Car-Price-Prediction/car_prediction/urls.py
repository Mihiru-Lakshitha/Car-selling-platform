from django.urls import path
from .views import predict_price

urlpatterns = [
    path('auctions/templates/', predict_price, name='predict_price'),
]
