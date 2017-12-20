# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/12/18'
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"]