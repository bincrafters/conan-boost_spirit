#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostSpiritConan(base.BoostBaseConan):
    name = "boost_spirit"
    url = "https://github.com/bincrafters/conan-spirit"
    lib_short_names = ["spirit"]
    header_only_libs = ["spirit"]
    b2_requires = [
        "boost_level11group",
    ]
