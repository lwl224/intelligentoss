# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2018/1/17'
"""
import sys

from tool.oss_data_treating import ScrapyDataAcquisition, Databases_dataSave

reload(sys)
sys.setdefaultencoding('utf8')


def test():
    print 123


def initializa():
    try:
        ScrapyDataAcquisition().get_original_data()
        Databases_dataSave().original_data_save()

    except:
        pass
