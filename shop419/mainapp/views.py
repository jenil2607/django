from django.shortcuts import render
from .models import Product

# to help to load template file
from django.template import loader

# to help return HTTP response to the user for any given request 
from django.http import HttpResponse

# importing the generic calss based viwes for CRUD operations

from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
def homeView(request):
    products = Product.objects.all()
    context = {
        'product_list' : products,
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def aboutView(request):
    context = {
        'current_page' : 'about'
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def contactsView(request):
    context = {
        'current_page' : 'view'
    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context, request))