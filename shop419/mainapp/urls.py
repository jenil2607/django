from django.urls import path

from .views import homeView, aboutView, contactsView

urlpatterns = [
    path("", homeView, name="homepage"),
    path("about", aboutView, name="aboutpage"),
    path("contacts", contactsView, name="contactspage")
] 
