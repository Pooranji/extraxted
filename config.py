#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7443034654:AAH83ai22x0R_um_D4zHToFIiCAv8M1q4Co")
    API_ID = int(os.environ.get("API_ID", "23940130"))
    API_HASH = os.environ.get("API_HASH", "4d717a6f888e37b7ebde0ace80cd22c6")
    AUTH_USERS = "5315677437"

