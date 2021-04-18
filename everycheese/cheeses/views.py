from django.views.generic import ListView, DetailView, CreateView


from .models import Cheese


class CheesesListView(ListView):
    model = Cheese


class CheesesDetailView(DetailView):
    model = Cheese


class CheeseCreateView(CreateView):
    model = Cheese

    fields = ["name", "description", "firmness", "country"]
