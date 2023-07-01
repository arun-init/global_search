from global_search.mixins.response import ResponseMixin
from rest_framework import generics


class GenericAPIViewMixin(ResponseMixin, generics.GenericAPIView):
    pass
