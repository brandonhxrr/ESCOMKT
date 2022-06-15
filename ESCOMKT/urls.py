"""ESCOMKT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler404
 
handler404 = views.error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeView.as_view(), name='home'),
    path('detail/<int:pk>/', views.detailProductView, name='detail_product'),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('', views.homeView.as_view(), name='start'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.profileView, name="profile"),
    path('crear/', views.CreateProductView.as_view(), name='create_product'),
    path('producto/<int:pk>/', views.EditProductView.as_view(), name='edit_product'),
    path('producto/delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)