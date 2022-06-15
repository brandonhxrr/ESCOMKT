from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate

from django import forms
from .models import Product
from .forms import ProductForm, ProductModelForm, ProductUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import Http404
from .mixins import IsMyProduct
from django.views.defaults import page_not_found

#def homeView(request):
 #   profile = Profile.objects.all()
  #  context = {'profile':profile}
   # return render(request, 'home/home.html', context)

def error_404(request, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response
 
    return page_not_found(request, template_name=nombre_template)

class homeView(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        #products = Product.objects.filter(user=self.request.user)
        products = Product.objects.all()
        return products

class userProductView(ListView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = Product.objects.all()
        return products

def detailProductView(request, pk):
    product = Product.objects.filter(id=pk)
    context = {'product':product}
    return render(request, 'products/detail.html', context)


class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = 'products/create_form_product.html'
    form_class = ProductModelForm
    success_url = '/'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.image = form.cleaned_data["image"]
        self.object.save()
        return super().form_valid(form)


class EditProductView(LoginRequiredMixin, IsMyProduct, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'products/detail_form_product.html'
    success_url = '/'


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/'

def profileView(request):
    products = Product.objects.filter(user = request.user)
    context = {'products':products}
    return render(request, 'home/profile.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    #success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    redirect_authenticated_user=True

    def form_valid(self, form):
        
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
