import logging

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from global_search.mixins.create_view import CreateAPIViewMixin
from global_search.models import User
from global_search.validators.phone_field import PhoneNumberField
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


def signup_page(request):
    return render(request, "signup.html")


class SignupAPI(CreateAPIViewMixin):
    """
    API endpoint for user signup.
    """

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=100)
        last_name = serializers.CharField(max_length=100, required=False)
        email = serializers.EmailField()
        phone = PhoneNumberField()
        gender = serializers.ChoiceField(choices=User.GenderChoices)

        def validate_email(self, value):
            if User.objects.filter(email_id=value).exists():
                raise serializers.ValidationError("User already exists for email")
            return value

        def validate_phone(self, value):
            if User.objects.filter(phone_number=value).exists():
                raise serializers.ValidationError("User already exists for phone number")
            return value

        def validate(self, attrs):
            attrs["username"] = attrs["email"]
            return attrs

    serializer_class = InputSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user signup.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = User.objects.create(
            first_name=data["first_name"],
            last_name=data.get("last_name", ""),
            gender=data["gender"],
            email_id=data["email"],
            phone_number=data["phone"],
            username=data["username"],
        )
        logger.info(f"User is created successfully: {user}")
        return self.success_response(
            data={"message": _("Account successfully created.")},
            status=status.HTTP_201_CREATED,
        )
