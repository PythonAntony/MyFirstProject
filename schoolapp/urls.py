from .import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("details/", views.details, name="details"),
    path("thanx/", views.thanx, name="thanx"),
    path("valuerepl/", views.valuerepl, name="valuerepl"),
    path("valuerepl/add/", views.addition, name="add"),
]
