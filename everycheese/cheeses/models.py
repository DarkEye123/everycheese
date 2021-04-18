from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django_countries.fields import CountryField


class Cheese(TimeStampedModel):
    def __str__(self) -> str:
        return "%s" % (self.name)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField("name of the Cheese", max_length=255)
    slug = AutoSlugField(
        "Cheese Address", unique=True, always_update=False, populate_from="name"
    )
    description = models.TextField("Description", blank=True)
    firmness = models.CharField(
        "Firmness",
        max_length=20,
        default=Firmness.UNSPECIFIED,
        choices=Firmness.choices,
    )
    country = CountryField(
        "Country of origin", blank_label="select country", blank=True
    )

    def get_absolute_url(self):
        return reverse("cheeses:detail", kwargs={"slug": self.slug})
