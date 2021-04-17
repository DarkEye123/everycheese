from django.urls import path

from . import views

app_name = "cheeses"

urlpatterns = [
    path(route="", view=views.CheesesListView.as_view(), name="list"),
    path(route="<slug:slug>/", view=views.CheesesDetailView.as_view(), name="detail"),
]
