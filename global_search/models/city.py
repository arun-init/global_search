from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name="id")
    Name = models.CharField(max_length=35, default="", verbose_name=_("name"))
    CountryCode = models.CharField(max_length=3, default="", verbose_name=_("country code"))
    District = models.CharField(max_length=20, default="", verbose_name=_("district"))
    Population = models.IntegerField(default=0, verbose_name=_("population"))

    class Meta:
        app_label = "global_search"
        db_table = "city"
        verbose_name = _("city")
        verbose_name_plural = _("city")

    def __str__(self):
        return f"City('name='{self.Name}')"

    def __repr__(self):
        return f"City('name='{self.Name}')"
