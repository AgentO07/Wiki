from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
 #   path("<str:name>", views.title, name="title"), 
    path("CreateNewPage", views.CreateNewPage, name="CreateNewPage"),
    path("RandomPage", views.RandomPage, name="RandomPage"),
    path("edit", views.edit, name="edit"),
    path("<str:name>", views.title, name="title")
]