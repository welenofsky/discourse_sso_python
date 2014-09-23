#! /usr/bin/python3
import urllib.parse
from hashlib import sha256
import hmac
from base64 import b64decode, b64encode

class DiscourseSSO:

    def __init__(self, secret_key):
        self.__secret_key = secret_key

    def validate(self, payload, sig):
        payload = urllib.parse.unquote(payload)
        computed_sig = hmac.new(self.__secret_key.encode(), payload.encode(), sha256).hexdigest()

        return hmac.compare_digest(computed_sig, sig)

    def get_nonce(self, payload):
        payload = b64decode(urllib.parse.unquote(payload)).decode()
        d = dict(nonce.split("=") for nonce in payload.split(' '))

        if 'nonce' in d and d['nonce'] != '':
            return d['nonce']
        else:
            raise Exception("Nonce could not be found in payload")

    def build_login_URL(self, credentials):
        reqs = ["external_id", "nonce", "email"]

        for r in reqs:
            if r not in credentials:
                e = "Missing required credential: '%s'" % r
                raise Exception(e)

        payload = urllib.parse.urlencode(credentials)
        payload = b64encode(payload.encode())
        sig = hmac.new(self.__secret_key.encode(), payload, sha256).hexdigest()

        return urllib.parse.urlencode({'sso': payload, 'sig': sig})