DiscourseSSO
====================

A Python module to help implement SSO for Discourse (http://www.discourse.org/)


**Features**
* validate() : Validates payload using HMAC-SHA256
* get_nonce() : Extracts Nonce from payload
* build_login_URL() : Generates login URL parameters given dictionary of credentials (More below)

Credentials for build_login_URL():


**required**
* external_id
* nonce
* email
    
**optional**
* email
* name

