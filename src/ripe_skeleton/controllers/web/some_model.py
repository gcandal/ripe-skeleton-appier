#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import ripe_skeleton

from . import adapter

class SomeModelController(adapter.AdapterController):

    @appier.route("/some_models/<int:id>", "GET")
    @appier.ensure(token = "admin")
    def show(self, id):
        some_model = ripe_skeleton.SomeModel.get(id = id)
        return self.template(
            "some_model/show.html.tpl",
            some_model = some_model
        )
