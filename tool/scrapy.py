# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/11/9'
"""

import sys
import urllib
import urllib2
import cookielib
import time
import os

reload(sys)
sys.setdefaultencoding('utf8')


class Abstract_ask():
    """oss操作抽象工厂类"""


    def __init__(self):
        Abstract_ask.get_new_cookie()
        pass

    @classmethod
    def get_new_cookie(cls):
        """获得cookie并保存"""
        oss_login_url = 'http://10.245.0.91:10101/wonop/login_check.action'
        username_password = {'userId': "chenhb35", 'password': "123"}
        cookie = cookielib.MozillaCookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
        urllib2.install_opener(opener)
        Abstract_ask.oss_loading_get_data(username_password, oss_login_url)
        cookie.save('cookie.txt', ignore_discard=True, ignore_expires=True)
        return True

    @classmethod
    def use_cookie(cls):
        """ 使用 get_new_cookie() 生成的cookie """
        cookie = cookielib.MozillaCookieJar()
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
        urllib2.install_opener(opener)

    @classmethod
    def make_time_flag(cls, para_dict, time_type='univ'):
        """
        增加时间戳
        :type para_dict: dict
        :type time_type: str

        """
        time_flag_now = time.time()
        time_flag = str(time_flag_now).split('.')[0]
        if time_type == 'univ':
            key_str = 'main_tain_query_' + time_flag
            para_dict['key'] = key_str
        if time_type == 'modify':
            str1 = time_flag + '000'
            para_dict[u'timestamp'] = str1

    @classmethod
    def oss_loading_get_data(cls, para_dict, url):
        """
        发送请求并获取数据
        :type para_dict: dict
        :type url: str
        """
        para_data = urllib.urlencode(para_dict)
        oss_req = urllib2.Request(url, para_data)
        oss_res = urllib2.urlopen(oss_req)
        return oss_res

    @classmethod
    def save_excel_file(cls, file_path, oss_res):
        """
        将oss应答数据保存
        :type file_path: str
        :type oss_res: response
        """
        abspath = os.path.abspath('.')
        if not os.path.exists('./' + file_path.split('/')[0]):
            os.makedirs('./' + file_path.split('/')[0])
        if not ('traffic1' in file_path):
            with open(file_path + '.xlsx', 'wb') as w_fh:
                w_fh.write(oss_res.read())
        else:
            with open(file_path + '.csv', 'wb') as w_fh:
                w_fh.write(oss_res.read())
        return True

    @classmethod
    def ask(cls, url, para_dict, file_path):
        pass


class Ask_save_excel(Abstract_ask):
    """获取表格数据具体操作类"""

    def __init__(self):
        Abstract_ask.__init__(self)

    @classmethod
    def ask(cls, url, para_dict, file_path):
        Ask_save_excel.make_time_flag(para_dict)
        oss_res = Ask_save_excel.oss_loading_get_data(para_dict, url)
        Ask_save_excel.save_excel_file(file_path, oss_res)
        return True


class Ask_modify(Abstract_ask):
    """更改oss对象具体操作类"""

    def __init__(self):
        Abstract_ask.__init__(self)

    @classmethod
    def ask(cls, url, para_dict, file_path):
        Ask_modify.make_time_flag(para_dict, 'modify')
        oss_res = Ask_modify.oss_loading_get_data(para_dict, url)
        res_msg = oss_res.read()
        res1 = res_msg.replace('\\', ' ').replace('\':', ' ').replace(',', ' ').split()
        return res1[1]


class Ask_delete(Abstract_ask):
    """删除oss对象具体操作类"""

    def __init__(self):
        Abstract_ask.__init__(self)

    @classmethod
    def ask(cls, url, para_dict, file_path):
        Ask_modify.make_time_flag(para_dict)
        oss_res = Ask_modify.oss_loading_get_data(para_dict, url)
        res_msg = oss_res.read()
        res1 = res_msg.replace('\\', ' ').replace('\':', ' ').replace(',', ' ').split()
        return res1[1]


def oss_ask(url, para_dict, file_path, asktyps=Ask_save_excel):
    """
    依照传入url进行请求
    :type para_dict: object
    :type url: str
    :type para_dict: object
    :type file_path: str
    :type asktyps: Abstract_ask
    """
    try:
        asktyps.ask(url, para_dict, file_path)
    except:
        pass
