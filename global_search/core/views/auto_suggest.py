from global_search.mixins.api_view import APIViewMixin
from global_search.models.city import City
from global_search.models.country import Country
from global_search.models.countrylanguage import CountryLanguage
from rest_framework import permissions, serializers, status


class AutoSuggestAPI(APIViewMixin):
    """
    API endpoint for auto-suggest functionality based on a search query.
    """

    class CountrySerializer(serializers.ModelSerializer):
        class Meta:
            model = Country
            fields = ["Name"]

    class CitySerializer(serializers.ModelSerializer):
        class Meta:
            model = City
            fields = ["Name"]

    class CountryLanguageSerializer(serializers.ModelSerializer):
        class Meta:
            model = CountryLanguage
            fields = ["Language"]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for auto-suggest functionality based on a search query.
        """
        query = request.query_params.get("query", "")
        if not query:
            return self.success_response(data={}, status=status.HTTP_200_OK)

        data = {
            "countries": self.CountrySerializer(
                Country.objects.filter(Name__istartswith=query), many=True
            ).data,
            "cities": self.CitySerializer(
                City.objects.filter(Name__istartswith=query), many=True
            ).data,
            "languages": self.CountryLanguageSerializer(
                CountryLanguage.objects.filter(Language__istartswith=query), many=True
            ).data,
        }

        return self.success_response(data=data, status=status.HTTP_200_OK)
