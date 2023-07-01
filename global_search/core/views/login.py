from django.contrib.auth import login
from django.shortcuts import render
from global_search.mixins.generic_view import GenericAPIViewMixin
from global_search.models import User
from global_search.utils import verify_otp
from global_search.validators.phone_field import PhoneNumberField
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny


def login_page(request):
    """
    Renders the login page.
    """
    return render(request, "login.html")


class LoginAPI(GenericAPIViewMixin):
    """
    API endpoint for user login with email or phone number and OTP.
    """

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=False)
        phone = PhoneNumberField(required=False)
        otp = serializers.CharField(max_length=4, min_length=4)

    serializer_class = InputSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user login with email or phone number and OTP.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data.get("email")
        phone = data.get("phone")
        otp = data.get("otp")

        user = None
        if email:
            user = User.objects.filter(email_id=email).first()
            key = user.email_id
        elif phone:
            user = User.objects.filter(phone_number=phone).first()
            key = user.phone_number

        if not user:
            return self.success_response(
                {"message": "Invalid email or phone number."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if verify_otp(key, otp):
            login(request, user)
            return self.success_response(
                {"message": "Login successful."}, status=status.HTTP_200_OK
            )
        else:
            raise serializers.ValidationError({"otp": "Invalid OTP"})
