#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import ripe_skeleton

from .. import adapter

class SomeModelAPIController(adapter.AdapterAPIController):

    @appier.route("/api/some_models", "GET", json = True)
    @appier.ensure(token = "some_models.read")
    def list(self):
        object = appier.get_object(alias = True, find = True, limit = 0)
        some_models = ripe_skeleton.SomeModel.find_v(map = True, **object)
        return some_models

    @appier.route("/api/some_models/<int:id>", "GET", json = True)
    @appier.ensure(token = "some_models.read")
    def show(self, id):
        some_model = ripe_skeleton.SomeModel.get(id = id, map = True)
        return some_model

    @appier.route("/api/some_models", "POST", json = True)
    @appier.ensure(token = "some_models.create")
    def create(self):
        some_model = ripe_skeleton.SomeModel.new()
        some_model.save()
        return some_model

    @appier.route("/api/some_models/<int:id>", "PUT", json = True)
    @appier.ensure(token = "some_models.update")
    def update(self, id):
        some_model = ripe_skeleton.SomeModel.get(id = id)
        some_model.apply()
        some_model.save()
        some_model = some_model.reload(map = True)
        return some_model

    @appier.route("/api/some_models/<int:id>", "DELETE", json = True)
    @appier.ensure(token = "some_models.delete")
    def delete(self, id):
        some_model = ripe_skeleton.SomeModel.get(id = id)
        some_model.delete()
        return some_model.map()
