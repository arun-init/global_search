from global_search.mixins.generic_view import GenericAPIViewMixin
from global_search.models import User
from global_search.utils import save_otp
from global_search.validators.phone_field import PhoneNumberField
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny


class MobileLoginSendOTPAPI(GenericAPIViewMixin):
    """
    API endpoint for sending OTP to the user's mobile number for login.
    """

    class InputSerializer(serializers.Serializer):
        phone = PhoneNumberField()

        def validate(self, attrs):
            phone = str(attrs["phone"]).lower()
            user = User.objects.filter(phone_number=phone).first()
            if not user:
                raise serializers.ValidationError("No user account found with this phone number")

            attrs["user"] = user
            return attrs

    permission_classes = [AllowAny]
    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for sending OTP to the user's mobile number for login.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        otp = save_otp(data.get("phone"), expires_in=600)
        # TODO: Add support to send SMS on mobile number using SMS Gateway
        return self.success_response(
            data={"message": f"We have sent an OTP to your mobile number successfully: {otp}"}
        )
