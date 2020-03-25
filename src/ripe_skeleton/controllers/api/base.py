#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

from . import adapter

class BaseAPIController(adapter.AdapterAPIController):

    @appier.route("/api/ping", "GET", json = True)
    def ping(self):
        return dict(time = time.time)
