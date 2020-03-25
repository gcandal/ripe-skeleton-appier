#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from . import base

class SomeModel(base.RipeSkeletonBase):

    field = appier.field(
        index = True,
        observations = """This is a description of the field"""
    )

    @classmethod
    def validate(cls):
        return super(SomeModel, cls).validate() + [
            appier.not_null("field"),
            appier.not_empty("field")
        ]

    @classmethod
    def list_names(cls):
        return ["field"]
