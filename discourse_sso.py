#! /usr/bin/python3

class Discourse_sso:
    def __init__(self, secret):
        self.__secret = secret
        print(self.__secret) 

    def validate(payload, sig):
	    pass
