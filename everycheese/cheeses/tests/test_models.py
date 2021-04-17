import pytest
from ..models import Cheese

pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name="test", firmness=Cheese.Firmness.HARD, description="meh"
    )
    assert cheese.__str__() == "test meh hard test"
    assert str(cheese) == "test meh hard test"
