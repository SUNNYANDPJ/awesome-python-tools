#!/usr/local/bin/env python
# encoding: utf-8


def find_attr(f_name, built_in_lib):
    '''
    import urllib2
    ast.find_attr('q', urllib2)

    result is quote
    '''
    r = filter(lambda b: b.startswith(f_name), dir(built_in_lib))
    return r if r else None
