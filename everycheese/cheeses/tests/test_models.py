import pytest
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def get_absolute_url():
    cheese = CheeseFactory()
    expected_url = f"/cheeses/{cheese.slug}/"
    assert cheese.get_absolute_url == expected_url
