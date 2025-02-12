from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth's user creation 


# Create your views here.

class userRagister(CreateView):
    
    template_name = 'register.html'
    success_url = reverse_lazy('signin')
