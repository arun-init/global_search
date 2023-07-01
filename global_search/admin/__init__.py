from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from global_search.models import User
from global_search.models.city import City
from global_search.models.country import Country
from global_search.models.countrylanguage import CountryLanguage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "email_id",
        "date_joined",
    )
    readonly_fields = ("date_joined",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email_id",
                    "phone_number",
                    "is_active",
                )
                + readonly_fields
            },
        ),
        (
            "Permissions options",
            {
                "classes": ("collapse",),
                "fields": ("is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
    )
    list_filter = ("is_active", "is_staff")
    search_fields = ("first_name", "last_name", "email_id")

    def title(self, obj):
        return f"User({obj.username})"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "Name",
        "CountryCode",
    )

    def title(self, obj):
        return f"City({obj.ID})"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "Code",
        "Name",
    )

    def title(self, obj):
        return f"Country({obj.Code})"


@admin.register(CountryLanguage)
class CountryLanguageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "Language",
        "CountryCode",
    )

    def title(self, obj):
        country_language = CountryLanguage.objects.filter(CountryCode=obj.CountryCode).first()
        return f"CountryLanguage({country_language.CountryCode})"
