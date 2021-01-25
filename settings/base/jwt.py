#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021-1-19

JWT_CONFIG = {
    'access_token_secret': 'ZS0s2iL1fyEomwFAOy+UroXoqlahmEEnye/v1ZoOQMb6zJh4Kwbbb9bx6sOnGH3q',
    'access_token_expires': 2592000,
    'access_token_leeway': 600,
    # 'refresh_token_secret': 'tYHqHD0E1NsSzvzQioz5OoFZiOQYBjKh65FjAFbrz369afMFjTgecFCWoA9nCOk7',
    # 'user_password_salt': 'fNjM9H0MoxWcHSIdvjTOotBmd1yy4TpxtNYtEPBdHqQaPjqTvCU75NpZiwwI5VXK',
    # 'refresh_token_expires': 15552000,
    # 'refresh_token_leeway': 600,
    # 'mongo_doc_ttl': 2592000,
    'jwt_header': {
        'alg': 'HS256',
        'typ': 'JWT'
        },
    # 'random_verify_code':{
    #     'secret': 'UUtY850qWu2UhfHfbIc8v2Tt06A7TJO3rLY31WfFp4SJYdSJQrqKVtrkDeLDWxP1',
    #     'expire': 600
    #     },
    }