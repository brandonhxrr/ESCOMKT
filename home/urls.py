from django.urls import path
from .views import homeView

urlpatterns = [
    path('', homeView, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    
]