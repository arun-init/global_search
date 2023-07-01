from django.contrib.auth import logout
from global_search.mixins.generic_view import GenericAPIViewMixin
from rest_framework import status


class LogoutAPI(GenericAPIViewMixin):
    """
    API endpoint for user logout.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user logout.
        """
        logout(request)
        return self.success_response({"message": "Logout successful."}, status=status.HTTP_200_OK)
