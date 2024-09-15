from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from TastyRecipesApp.profiles.models import Profile


class Recipe(models.Model):
    class CuisineChoices(models.TextChoices):
        FRENCH = "French"
        CHINESE = "Chinese"
        ITALIAN = "Italian"
        BALKAN = "Balkan"
        OTHER = "Other"

    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 10
    CUISINE_MAX_LENGTH = 7

    title = models.CharField(
        unique=True,
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
        ],
        null=False,
        blank=False,
    )

    cuisine_type = models.CharField(
        max_length=CUISINE_MAX_LENGTH,
        null=False,
        blank=False,
        choices=CuisineChoices.choices,
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
        null=False,
        blank=False,
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),  # Cooking time must be at least 1 minute.
        ],
        help_text="Provide the cooking time in minutes.",
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )