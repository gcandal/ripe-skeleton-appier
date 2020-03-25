#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class RipeSkeletonApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "ripe_skeleton",
            locales = ("en_us",),
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )
        self.logo_url = self.logo_url or\
            self.url_for("static", filename = "images/logo_crop.svg")
        self.logo_square_url = self.logo_square_url or\
            self.url_for("static", filename = "images/logo_square.svg")
        self.logo_raster_url = self.logo_raster_url or\
            self.url_for("static", filename = "images/logo.png")
        self.favicon_url = self.favicon_url or\
            self.url_for("static", filename = "images/favicon.png")
        self.config = dict(
            cache = not self.is_devel(),
            footer = self.is_devel() or True
        )

    def _description(self):
        return "RIPE Skeleton"

    def _observations(self):
        return "RIPE Skeleton for Appier applications"

if __name__ == "__main__":
    app = RipeSkeletonApp()
    app.serve()
else:
    __path__ = []
