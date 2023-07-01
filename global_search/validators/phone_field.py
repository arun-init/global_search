from django.conf import settings
from django.utils.translation import gettext_lazy as _
from global_search.validators.utils import format_mobile_number, is_valid_mobile_number
from rest_framework import serializers


class MobileNumberLengthInvalid(Exception):
    pass


class CallingCodeInvalid(Exception):
    pass


class PhoneNumberField(serializers.CharField):
    """
    A mobile number field for doing format validation and also do calling
    code support check for system and return international formatted mobile
    number
    """

    default_error_messages = {
        "invalid_mobile_number": _("Not a valid mobile number."),
        "invalid_calling_code": _("Not a valid calling code in mobile number"),
        "system_not_support_calling_code": _(
            "Calling code {calling_code} is not supported by system"
        ),
        "invalid_mobile_number_length": _("Mobile number length is invalid"),
    }

    def __init__(self, **kwargs):
        self.cc_support_check = kwargs.pop("cc_support_check", True)
        super().__init__(**kwargs)

    def get_default_calling_code(self):
        return settings.DEFAULT_CALLING_CODE

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        default_calling_code = self.get_default_calling_code()
        cc_support_check = self.cc_support_check
        try:
            if not is_valid_mobile_number(
                mobile_number=data,
                calling_code=default_calling_code,
                cc_support_check=cc_support_check,
            ):
                self.fail("invalid_mobile_number")
        except MobileNumberLengthInvalid:
            self.fail("invalid_mobile_number_length")
        except CallingCodeInvalid:
            self.fail("invalid_calling_code")

        mobile_number = format_mobile_number(data, calling_code=default_calling_code)

        return mobile_number
