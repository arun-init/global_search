import hashlib
import json

from django.core.cache import cache
from django.utils.crypto import constant_time_compare, get_random_string


def hash_hex(value):
    """
    Returns MD5 hash in hexadecimal form. This hash is fixed size of 32
    characters. MD5 is not secure hashing algorithm, so don't use this hash
    at sensitive places.

    :param value: string or bytes
    :return: hash string
    """
    if not isinstance(value, bytes):
        value = json.dumps(value).encode("utf-8")
    # deepcode ignore insecureHash: we are not using at sensitive places
    return hashlib.md5(value).hexdigest()  # nosec


def generate_otp(length=4, allowed_chars="0123456789"):
    """Generates a random otp for given length"""
    return get_random_string(length, allowed_chars=allowed_chars)


def get_otp_key(key, namespace=None, secure_key=True):
    """Generate an otp key"""
    if secure_key:
        # this we're doing for obfuscating otp key
        key = hash_hex(key)
    otp_key = ":".join([namespace or "", key])
    return otp_key


def save_otp(key, otp=None, expires_in=60, namespace=None):
    """Store OTP to storage for given expiry time.

    * Expiry time is in seconds.
    * You can also pass namespace to categorize otp for same key.
    * Either pass otp or it will generate fresh otp
    """
    otp_key = get_otp_key(key, namespace)
    otp = otp or generate_otp()
    cache.set(otp_key, value=otp, timeout=expires_in)
    return otp


def verify_otp(key, otp, namespace=None, clear_on_verified=True):
    """Verify given otp with saved otp for the key.

    This also clear the stored valid otp from store. You can manage it by setting
    `clear_on_verified` flag.
    """
    otp_key = get_otp_key(key, namespace)
    valid_otp = cache.get(otp_key)
    is_verified = False
    if valid_otp and otp and constant_time_compare(str(valid_otp), str(otp)):
        is_verified = True
    if is_verified and clear_on_verified:
        cache.delete(otp_key)
    return is_verified
