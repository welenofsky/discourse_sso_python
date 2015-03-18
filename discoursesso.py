#! /usr/bin/python3
import urllib.parse
from hashlib import sha256
import hmac
from base64 import b64decode, b64encode


class DiscourseSSO:

    def __init__(self, secret_key):
        self.__secret_key = secret_key

    def validate(self, payload, sig):
        """ Validates payload using HMAC-SHA256

        :param payload:
            Payload string from URL
        :param sig:
            Signature string from URL

        :return:
            Bool : Indicates validity of payload
        """
        payload = urllib.parse.unquote(payload)
        computed_sig = hmac.new(
            self.__secret_key.encode(),
            payload.encode(),
            sha256
        ).hexdigest()

        return hmac.compare_digest(computed_sig, sig)

    def get_nonce(self, payload):
        """ Extracts Nonce from payload

            :param payload:
                Base64 encoded string comprising of a nonce

            :return:
                string : Nonce extracted from payload

        """
        payload = b64decode(urllib.parse.unquote(payload)).decode()
        d = dict(nonce.split("=") for nonce in payload.split('&'))

        if 'nonce' in d and d['nonce'] != '':
            return d['nonce']
        else:
            raise Exception("Nonce could not be found in payload")

    def build_login_URL(self, credentials):
        """ Generates login URL parameters

        :param:
            credentials : Dictionary of user credentials
                required keys
                    * external_id
                    * nonce
                    * email
                optional keys
                    * email
                    * name

        :return:
            string: URL Parameters for login URL
                ex: sig=f0f8ede4daa7627...&sso=bm9uY2U9YW9kMGY5YWh...
                    (EXAMPLE SHORTENED FOR READABILITY)
        """
        reqs = ["external_id", "nonce", "email"]

        for r in reqs:
            if r not in credentials:
                e = "Missing required credential: '%s'" % r
                raise Exception(e)

        payload = urllib.parse.urlencode(credentials)
        payload = b64encode(payload.encode())
        sig = hmac.new(self.__secret_key.encode(), payload, sha256).hexdigest()

        return urllib.parse.urlencode({'sso': payload, 'sig': sig})
