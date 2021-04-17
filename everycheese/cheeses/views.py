from django.views.generic import ListView, DetailView

from .models import Cheese


class CheesesListView(ListView):
    model = Cheese


class CheesesDetailView(DetailView):
    model = Cheese
