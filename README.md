DiscourseSSO
====================

A Python module to help implement SSO for Discourse (http://www.discourse.org/). For additional information on how to use SSO see https://meta.discourse.org/t/official-single-sign-on-for-discourse/13045

Helper Functions
-------------------
* validate() : Validates payload using HMAC-SHA256
* get_nonce() : Extracts Nonce from payload
* build_login_URL() : Generates login URL parameters given dictionary of credentials (More below)

How to Use
---------------------

```python
from discoursesso import DiscourseSSO

sso = DiscourseSSO(secret_key)

# Get Payload and Signature from incoming GET request
## Payload (sso=...) from URL discourse gave you
payload = "bm9uY2U9Y2I2ODI1MWVlZmI1MjExZTU4YzAwZmYxMzk1ZjBjMGI%3D%0A"
## Signature (sig=...) from URL discourse gave you
sig = "2828aa29899722b35a2f191d34ef9b3ce695e0e6eeec47deb46d588d70c7cb56"

# Validate a payload/sig, EX
if sso.validate(payload, sig):
    # Get users login credentials and build the URL to log the user 
    # into your discourse site. ex: discourse.example.com
    ## credentials is a Dictionary of user credentials, see below
    ## for more information on how to build the Dictionary
    return_url_base = "http://discuss.example.com/session/sso_login?%s"
    loginURL =  return_url_base % sso.build_login_URL(credentials)
```


Credentials for build_login_URL():
--------------------
**required**
* external_id
* nonce
* email
    
**optional**
* email
* name

