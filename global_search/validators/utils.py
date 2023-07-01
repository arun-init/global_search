import re

from django.conf import settings

MOBILE_NUMBER_WITHOUT_CC_REGEX = re.compile("^(\\d{4,12})$")
MOBILE_NUMBER_CC_REGEX = re.compile("^\\+(\\d{1,3}) (\\d{4,12})$")
MOBILE_NUMBER_REGEX = re.compile("^\\+(\\d*) (\\d*)$")


def is_valid_mobile_number_without_cc(mobile_number):
    return MOBILE_NUMBER_WITHOUT_CC_REGEX.match(str(mobile_number)) is not None


def is_valid_mobile_number_with_cc(mobile_number):
    return MOBILE_NUMBER_CC_REGEX.match(str(mobile_number)) is not None


def normalize_mobile_number(mobile_number, calling_code):
    """
    Normalize the given mobile number to the international format
    (i.e +<calling code> <mobile number>) if possible otherwise return empty
    string
    :param mobile_number:
    :param calling_code: default calling code for mobile number have missing
    calling code
    :return:
    """
    mobile_number = str(mobile_number)
    if is_valid_mobile_number_with_cc(mobile_number):
        return mobile_number
    elif is_valid_mobile_number_without_cc(mobile_number):
        return "+%s %s" % (calling_code, mobile_number)
    return


def split_cc_and_mobile_number(mobile_number):
    """
    Extract calling code and mobile number digits from given mobile number.
    Note: It doesn't do validation, please validate the mobile number first,
    if not sure.
    :param mobile_number: a mobile number
    :return: a tuple of calling code and mobile number digits
    """
    m = MOBILE_NUMBER_REGEX.match(str(mobile_number))
    return m.group(1), m.group(2)


def format_mobile_number(mobile_number: str, calling_code: str = None) -> str:
    """
    Format given mobile number by normalizing it to international format if
    possible otherwise return same mobile number
    :param mobile_number: mobile number
    :param calling_code: default calling code for mobile number have missing
    calling code
    :return: mobile number
    """
    m = normalize_mobile_number(mobile_number, calling_code=calling_code)
    # normalization return empty string for invalid mobile number format
    if not m:
        m = mobile_number
    return m


def is_valid_mobile_number(mobile_number, calling_code=None, cc_support_check=True):
    """
    Checks whether the given mobile number is in any supported formats (i.e
    with cc or without cc). Can raise `CallingCodeInvalid` error on finding
    invalid calling code. Can also raise `CallingCodeNotSupported` error if
    calling code is not supported by the system. Can also raise
    `MobileNumberLengthInvalid` error if mobile number is not valid as per
    country specs
    :param mobile_number: mobile number
    :param calling_code: default calling code for mobile number have missing
    calling code
    :param cc_support_check: do calling code support check
    :return: boolean
    """
    if calling_code is None:
        calling_code = settings.DEFAULT_CALLING_CODE
    mobile_number = normalize_mobile_number(mobile_number, calling_code=calling_code)

    if not mobile_number:
        return False

    cc, mobile_number_without_cc = split_cc_and_mobile_number(mobile_number)

    return True
