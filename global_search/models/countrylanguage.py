from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from global_search.models.country import Country


class CountryLanguage(models.Model):
    COUNTRY_CODE_CHOICES = (
        ("T", "T"),
        ("F", "F"),
    )
    CountryCode = models.CharField(max_length=3, primary_key=True, verbose_name="Country Code")
    Language = models.CharField(max_length=30, verbose_name="Language")
    IsOfficial = models.CharField(
        max_length=1,
        choices=COUNTRY_CODE_CHOICES,
        default="F",
        verbose_name="Is Official",
    )
    Percentage = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        verbose_name="Percentage",
    )

    class Meta:
        app_label = "global_search"
        db_table = "countrylanguage"
        verbose_name = _("country language")
        verbose_name_plural = _("country languages")
        constraints = [
            models.UniqueConstraint(
                fields=("CountryCode", "Language"), name="country_language_unique"
            ),
            models.UniqueConstraint(fields=("CountryCode",), name="countryLanguage_ibfk_1"),
        ]

    def __str__(self):
        return f"CountryLanguage('name='{self.CountryCode}')"

    def __repr__(self):
        return f"CountryLanguage('name='{self.CountryCode}')"
