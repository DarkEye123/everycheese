from django.forms.forms import BaseForm
from django.http.response import HttpResponse
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

    def form_valid(self, form: BaseForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)
