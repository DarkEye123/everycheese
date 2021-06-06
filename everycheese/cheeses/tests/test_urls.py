import pytest

from django.urls import reverse, resolve

from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def cheese():
    return CheeseFactory()


def test_cheeses_list_reverse():
    assert reverse("cheeses:list") == "/cheeses/"


def test_cheeses_list_resolve():
    assert resolve("/cheeses/").view_name == "cheeses:list"


def test_cheeses_create_reverse():
    assert reverse("cheeses:add") == "/cheeses/add/"


def test_cheeses_create_resolve():
    assert resolve("/cheeses/add/").view_name == "cheeses:add"


def test_cheeses_detail_reverse(cheese):
    assert (
        reverse("cheeses:detail", kwargs={"slug": cheese.slug})
        == f"/cheeses/{cheese.slug}/"
    )


def test_cheeses_detail_resolve(cheese):
    assert resolve(f"/cheeses/{cheese.slug}/").view_name == "cheeses:detail"