from django.db import models

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class Cheese(TimeStampedModel):
    def __str__(self) -> str:
        return "%s %s %s %s" % (self.name, self.description, self.firmness, self.slug)

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
