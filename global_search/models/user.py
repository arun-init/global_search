from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        PREFER_NOT_TO_SAY = ("", _("Prefer Not to Say"))

    first_name = models.CharField(max_length=100, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, blank=True, verbose_name=_("Last Name"))
    gender = models.CharField(
        max_length=20,
        choices=GenderChoices.choices,
        verbose_name=_("gender"),
    )
    email_id = models.EmailField(
        primary_key=True,
        blank=True,
        validators=[validate_email],
        verbose_name=_("email address"),
    )
    phone_number = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_("phone number"),
    )

    class Meta:
        app_label = "global_search"
        db_table = "global_search_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return f"User('email='{self.email}')"

    def __repr__(self) -> str:
        return f"User('email='{self.email}')"
