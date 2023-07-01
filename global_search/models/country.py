from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    CODE_CHOICES = (
        ("Asia", "Asia"),
        ("Europe", "Europe"),
        ("North America", "North America"),
        ("Africa", "Africa"),
        ("Oceania", "Oceania"),
        ("Antarctica", "Antarctica"),
        ("South America", "South America"),
    )

    Code = models.CharField(max_length=3, primary_key=True, verbose_name="Country Code")
    Name = models.CharField(max_length=52, default="", verbose_name="Country Name")
    Continent = models.CharField(
        max_length=15, choices=CODE_CHOICES, default="Asia", verbose_name="Continent"
    )
    Region = models.CharField(max_length=26, default="", verbose_name="Region")
    SurfaceArea = models.FloatField(default=0.00, verbose_name="Surface Area")
    IndepYear = models.SmallIntegerField(null=True, blank=True, verbose_name="Year of Independence")
    Population = models.IntegerField(default=0, verbose_name="Population")
    LifeExpectancy = models.FloatField(null=True, blank=True, verbose_name="Life Expectancy")
    GNP = models.FloatField(null=True, blank=True, verbose_name="GNP")
    GNPOld = models.FloatField(null=True, blank=True, verbose_name="GNP Old")
    LocalName = models.CharField(max_length=45, default="", verbose_name="Local Name")
    GovernmentForm = models.CharField(max_length=45, default="", verbose_name="Government Form")
    HeadOfState = models.CharField(
        max_length=60, null=True, blank=True, verbose_name="Head of State"
    )
    Capital = models.IntegerField(null=True, blank=True, verbose_name="Capital")
    Code2 = models.CharField(max_length=2, default="", verbose_name="Country Code 2")

    class Meta:
        app_label = "global_search"
        db_table = "country"
        verbose_name = _("country")
        verbose_name_plural = _("country")

    def __str__(self):
        return f"Country('name='{self.Name}')"

    def __repr__(self):
        return f"Country('name='{self.Name}')"
