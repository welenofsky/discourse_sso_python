#! /usr/bin/python3

from discoursesso import DiscourseSSO

"""
These are the credentials used in the example
    https://meta.discourse.org/t/official-single-sign-on-for-discourse/13045
"""
payload = "bm9uY2U9Y2I2ODI1MWVlZmI1MjExZTU4YzAwZmYxMzk1ZjBjMGI%3D%0A"
secret_key = "d836444a9e4084d5b224a60c208dce14"
sig = "2828aa29899722b35a2f191d34ef9b3ce695e0e6eeec47deb46d588d70c7cb56"


min_req_credentials = {
    "external_id": "welenofsky",
    "nonce": "aod0f9ahdfha9d8hf8a",
    "email": "email@example.com"
}

sso = DiscourseSSO(secret_key)

sso.validate(payload, sig)
print("Nonce From Payload: ",    sso.get_nonce(payload))
print("Generated Login URL:")
print("http://discuss.example.com/session/sso_login?%s" % sso.build_login_URL(min_req_credentials))