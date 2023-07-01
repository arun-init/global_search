from global_search.mixins.api_view import APIViewMixin
from global_search.models.city import City
from global_search.models.country import Country
from global_search.models.countrylanguage import CountryLanguage
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated


class SearchAPI(APIViewMixin):
    """
    API endpoint for searching cities, countries, and languages based on a query.
    """

    class CountrySerializer(serializers.ModelSerializer):
        class Meta:
            model = Country
            fields = ["Code", "Name", "Continent", "Capital"]

    class CitySerializer(serializers.ModelSerializer):
        class Meta:
            model = City
            fields = ["Name", "CountryCode", "District"]

    class CountryLanguageSerializer(serializers.ModelSerializer):
        class Meta:
            model = CountryLanguage
            fields = ["Language"]

    class InputSerializer(serializers.Serializer):
        query = serializers.CharField()

    serializer_class = InputSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for searching cities, countries, and languages based on a query.
        """
        query = request.GET.get("query", "")

        if not query:
            return self.success_response(data="", status=status.HTTP_200_OK)

        countries = Country.objects.filter(Name__istartswith=query)
        cities = City.objects.filter(Name__istartswith=query)
        languages = CountryLanguage.objects.filter(Language__istartswith=query)

        country_serializer = self.CountrySerializer(countries, many=True)
        city_serializer = self.CitySerializer(cities, many=True)
        language_serializer = self.CountryLanguageSerializer(languages, many=True)

        data = {
            "cities": city_serializer.data,
            "countries": country_serializer.data,
            "languages": language_serializer.data,
        }

        return self.success_response(data=data, status=status.HTTP_200_OK)
