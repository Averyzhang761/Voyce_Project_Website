from django.contrib.auth.tokens import PasswordResetTokenGenerator

import six
from django.utils.crypto import salted_hmac, constant_time_compare
from django.utils.http import int_to_base36, base36_to_int

from datetime import datetime

def to_integer(dt_time):
    return int(100000000*dt_time.year + 1000000*dt_time.month + 10000*dt_time.day + 100*dt_time.hour + dt_time.minute)

class ResetPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _num_seconds(self, dt):

        #return int((dt - datetime(2001, 1, 1)).total_seconds())

        return to_integer(dt)


    def _now(self):
        # Used for mocking in tests
        return datetime.now()

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
        #print(timestamp)

        ts_b36 = int_to_base36(timestamp)
        # print(timestamp)
        #print(timestamp)
        hash = salted_hmac(
            self.key_salt,
            self._make_hash_value(user, timestamp),
        ).hexdigest()[::2]
        return "%s-%s" % (ts_b36, hash)

    def _make_token_with_timestamp_fixed(self, user, timestamp, legacy=True):
        # timestamp is number of days since 2001-1-1.  Converted to
        # base 36, this gives us a 3 digit string until about 2121

        # current_datetime = datetime.now()
        # timestamp = to_integer(current_datetime)
        #print(timestamp)

        ts_b36 = int_to_base36(timestamp)
        # print(timestamp)
        #print(timestamp)
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
            new_ts = int(str(ts)[:12])
            print(new_ts, "this is the new ts")
        except ValueError:
            return False

        # Check that the timestamp/uid has not been tampered with
        if not constant_time_compare(self._make_token_with_timestamp_fixed(user, ts), token):
            # RemovedInDjango40Warning: when the deprecation ends, replace
            # with:
            #   return False
            if not constant_time_compare(
                    self._make_token_with_timestamp_fixed(user, ts, legacy=True),
                    token,
            ):

                #print(token, self._make_token_with_timestamp(user, ts, legacy=True))
                return False
        print("pass through")
        # Check the timestamp is within limit.
        from django.conf import settings
        print(self._num_seconds(self._now()))
        print(ts ,"this is the new timestamp")
        if (self._num_seconds(self._now()) - ts) > settings.PASSWORD_RESET_TIMEOUT:
            print(self._num_seconds(self._now()))
            #print(ts)
            print("timeout")
            return False

        return True

reset_password_Generator = ResetPasswordResetTokenGenerator()


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmed)
        )


account_activation_token = AccountActivationTokenGenerator()