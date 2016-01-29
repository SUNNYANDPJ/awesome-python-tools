#!/usr/local/bin/env python
# encoding: utf-8


def function_exists(f_name, built_in_lib):
    return f_name in filter(lambda b: b.startswith(f_name), dir(built_in_lib))
