from django.contrib.auth.tokens import PasswordResetTokenGenerator

import six
from django.utils.crypto import salted_hmac, constant_time_compare
from django.utils.http import int_to_base36, base36_to_int

from datetime import datetime

def to_integer(dt_time):
    return int(10000*dt_time.year + 100*dt_time.month + dt_time.day + dt_time.second)

class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):

        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email)
        )

    def _make_token_with_timestamp(self, user, timestamp, legacy=False):
        # timestamp is number of days since 2001-1-1.  Converted to
        # base 36, this gives us a 3 digit string until about 2121
        current_datetime = datetime.now()
        timestamp = to_integer(current_datetime)
        ts_b36 = int_to_base36(timestamp)
        # print(timestamp)
        print(timestamp)
        hash = salted_hmac(
            self.key_salt,
            self._make_hash_value(user, timestamp),
        ).hexdigest()[::2]
        return "%s-%s" % (ts_b36, hash)

    def check_token(self, user, token):
        """
        Check that a password reset token is correct for a given user.
        """
        if not (user and token):
            return False
        # Parse the token
        try:
            ts_b36, _ = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        # Check that the timestamp/uid has not been tampered with
        # if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):
        #     # RemovedInDjango40Warning: when the deprecation ends, replace
        #     # with:
        #     #   return False
        #     if not constant_time_compare(
        #             self._make_token_with_timestamp(user, ts, legacy=True),
        #             token,
        #     ):
        #
        #         print(token, self._make_token_with_timestamp(user, ts, legacy=True))
        #         return False

        # Check the timestamp is within limit.
        from django.conf import settings
        # if (self._num_seconds(self._now()) - ts) > settings.PASSWORD_RESET_TIMEOUT:
        #     return False

        return True

my_password_Generator = MyPasswordResetTokenGenerator()