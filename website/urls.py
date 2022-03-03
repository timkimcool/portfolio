from django.urls import path
from .views import HomePageView, OriginalView

urlpatterns = [
    path('original/', OriginalView.as_view(), name='original'),
    path('', HomePageView.as_view(), name='home'),
]