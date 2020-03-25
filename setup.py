#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name = "ripe-skeleton",
    version = "0.1.0",
    author = "Platforme International",
    author_email = "development@platforme.com",
    description = "RIPE ID",
    license = "Apache License, Version 2.0",
    keywords = "ripe id",
    url = "https://www.platforme.com",
    zip_safe = False,
    packages = [
        "ripe_skeleton",
        "ripe_skeleton.controllers",
        "ripe_skeleton.controllers.api",
        "ripe_skeleton.controllers.web",
        "ripe_skeleton.models",
        "ripe_skeleton.test",
        "ripe_skeleton.test.models",
    ],
    test_suite = "ripe_skeleton.test",
    package_dir = {
        "" : os.path.normpath("src")
    },
    install_requires = [
        "appier",
        "appier_extras",
        "jinja2",
        "pymongo"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
