#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        boost_deps = ['algorithm', 'array', 'assert', 'concept_check', 'config', 'core', 'endian', 'filesystem', 'foreach', 'function', 'function_types', 'fusion', 'integer', 'io', 'iostreams', 'iterator', 'lexical_cast', 'locale', 'math', 'move', 'mpl', 'optional', 'phoenix', 'predef', 'preprocessor', 'proto', 'range', 'regex', 'smart_ptr', 'spirit', 'static_assert', 'throw_exception', 'tti', 'type_traits', 'typeof', 'unordered', 'utility', 'variant']
        for lib in boost_deps:
            self.requires("boost_" + lib + "/1.67.0@" + self.user + "/" + self.channel)
        if False:
            if not tools.os_info.is_windows:
                self.requires("openmpi/3.0.0@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            if self.settings.os == "Windows":
                self.run(os.path.join("bin", "test_package"))
            else:
                self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ['DYLD_LIBRARY_PATH'], os.path.join("bin", "test_package")))
