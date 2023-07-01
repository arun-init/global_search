from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from global_search.mixins.generic_view import GenericAPIViewMixin
from global_search.models.city import City
from global_search.models.country import Country
from global_search.models.countrylanguage import CountryLanguage
from rest_framework import permissions, serializers, status


@login_required
def detail_page(request):
    """
    Renders the detail page.
    """
    return render(request, "detail.html")


class DetailAPI(GenericAPIViewMixin):
    """
    API endpoint for retrieving details based on the search query.
    """

    class CountrySerializer(serializers.ModelSerializer):
        class Meta:
            model = Country
            fields = "__all__"

    class CitySerializer(serializers.ModelSerializer):
        class Meta:
            model = City
            fields = "__all__"

    class CountryLanguageSerializer(serializers.ModelSerializer):
        class Meta:
            model = CountryLanguage
            fields = "__all__"

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for retrieving details based on the search query.
        """
        query = request.query_params.get("query", "")
        if not query:
            return self.success_response(data="", status=status.HTTP_200_OK)

        result = {}
        models = [City, Country]
        serializers = [self.CitySerializer, self.CountrySerializer]

        for model, serializer_class in zip(models, serializers):
            queryset = model.objects.filter(Name=query)
            if queryset:
                result = serializer_class(queryset, many=True).data
                break

        country_language_qs = CountryLanguage.objects.filter(Language=query)
        if country_language_qs:
            result = self.CountryLanguageSerializer(country_language_qs, many=True).data

        return self.success_response(data=result, status=status.HTTP_200_OK)
