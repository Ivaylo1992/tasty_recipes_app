from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipesApp.profiles.validators import validate_user_names


class Profile(models.Model):
    NICKNAME_MAX_LENGTH = 20
    NICKNAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    nickname = models.CharField(
        max_length=NICKNAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NICKNAME_MIN_LENGTH),
        ],
        null=False,
        blank=False,
        error_messages={
            "unique": "Nickname must be at least 2 chars long!",
        },
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_user_names,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            validate_user_names,
        ],
    )

    chef = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )



