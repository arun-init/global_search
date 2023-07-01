from global_search.mixins.response import ResponseMixin
from rest_framework import views


class APIViewMixin(ResponseMixin, views.APIView):
    pass
