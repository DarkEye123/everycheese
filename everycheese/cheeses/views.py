from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cheese


class CheesesListView(ListView):
    model = Cheese


class CheesesDetailView(DetailView):
    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese

    fields = ["name", "description", "firmness", "country"]
