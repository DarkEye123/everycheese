from everycheese.cheeses.models import Cheese
import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse

from .factories import CheeseFactory
from .factories import UserFactory

from ..views import CheesesListView, CheesesDetailView

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserFactory()


# rf is shortcut for django.test.RequestFactory
def test_cheeses_list_view(rf):
    url = reverse("cheeses:list")
    request = rf.get(url)
    callable_obj = CheesesListView.as_view()
    response = callable_obj(request)
    assertContains(response, "Cheese List")


def test_cheeses_list_view_multiple_cheeses(rf):
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()
    url = reverse("cheeses:list")
    request = rf.get(url)
    response = CheesesListView.as_view()(request)
    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)


def test_cheeses_detail(rf):
    cheese = CheeseFactory()
    url = reverse("cheeses:detail", kwargs={"slug": cheese.slug})
    request = rf.get(url)
    response = CheesesDetailView.as_view()(request, slug=cheese.slug)
    assert response.status_code == 200
    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country.name)


def cheeses_create_view(client, user):
    form_data = {
        "name": "test cheese",
        "description": "test description",
        "firmness": Cheese.Firmness.HARD,
    }
    client.force_login(user)
    url = reverse("cheeses:add")
    response = client.post(url, form_data)
    assert response.status_code == 302

    cheese = Cheese.objects.get(name="test cheese")
    assert cheese.description == form_data.description
    assert cheese.firmness == form_data.firmness
    assert cheese.creator == user
