from global_search.mixins.response import ResponseMixin
from rest_framework import generics


class CreateAPIViewMixin(ResponseMixin, generics.CreateAPIView):
    pass
