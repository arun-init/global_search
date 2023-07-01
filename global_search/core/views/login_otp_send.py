from global_search.mixins.generic_view import GenericAPIViewMixin
from global_search.models import User
from global_search.utils import save_otp
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny


class EmailLoginSendOTPAPI(GenericAPIViewMixin):
    """
    API endpoint for sending OTP to the user's email for email login.
    """

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()

        def validate(self, attrs):
            email = str(attrs["email"]).lower()
            user = User.objects.filter(email_id=email).first()
            if not user:
                raise serializers.ValidationError("No user account found with this email")

            attrs["user"] = user
            return attrs

    permission_classes = [AllowAny]
    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for sending OTP to the user's email.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        otp = save_otp(data.get("email"), expires_in=600)
        # TODO: Added support to send email but
        # according to new guidelines now you can't use your
        # personal email account to test emails
        # send_verify_email_otp(data["user"],template,context)

        return self.success_response(
            data={"message": f"We have sent an OTP to your email successfully: {otp}"}
        )
