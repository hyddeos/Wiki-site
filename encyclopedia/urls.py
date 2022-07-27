from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage.html", views.newpage, name="newpage"),
    path("editpage.html", views.editpage, name="editpage"),
    path("random.html", views.random_entry, name="random"),
    path("search/", views.search, name="search"),    
    path("<str:subject>", views.wiki, name="wiki")    
]

