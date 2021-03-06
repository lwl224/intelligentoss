# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/12/9'
"""
import sys
import os
import xlrd
from gevent import monkey
import gevent
import time
from tool.scrapy import oss_ask, AbstractAsk
import shutil

import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intelligentoss.settings")
    django.setup()

monkey.patch_socket()

reload(sys)
sys.setdefaultencoding('utf8')
start = time.clock()


class AbstractDataAcquisition:
    def __init__(self):
        pass

    def get_original_data(self):
        raise NotImplementedError

    def delete_original_data(self):
        raise NotImplementedError


class AbstractDataSave:
    def __init__(self):
        pass

    def original_data_save(self):
        raise NotImplementedError

    def delete_savedata(self):
        raise NotImplementedError


class Databases_dataSave(AbstractDataSave):
    def original_data_save(self):
        all_flag = True
        save_data_lsit = [(self.save2databases, 'Bbu', 'data/bbu.xlsx', [6, 7]),
                          (self.save2databases, 'Ltecell', 'data/cell.xlsx', [14, 15]),
                          (self.save2databases, 'Antenna', 'data/antenna.xlsx', [5, 6, 10, 11]),
                          (self.save2databases, 'Cell2scenes', 'data/cell2scenes.xlsx', [0]),
                          (self.save2databases, 'Scenes', 'data/scenes.xlsx', [8, 9, 14, 15]),
                          (self.save2databases, 'Enodeb', 'data/enodeb.xlsx', [34, 35]),
                          (self.save2databases, 'Rru', 'data/rru.xlsx', [5, 6]),
                          (self.save2databases, 'Physicalstation', 'data/physicalstation.xlsx', [6, 7]), ]
        try:
            for save_data_example in save_data_lsit:
                gevent_save = apply(gevent.spawn, save_data_example)
                gevent_save.join()
                all_flag = all_flag & gevent_save.successful()
            return all_flag
        except:
            raise LookupError


    def delete_savedata(self):
        pass


    @staticmethod
    def save2databases(class_name='Ltecell', file_name='cell.xlsx', check_rows=None):
        if check_rows is None:
            check_rows = [14, 15]
        save_data_class = None
        load_models = sys.modules['smart_import.models']  # 得到这个模块
        class_list = dir(load_models)  # 得到属性的列表
        for test_class in class_list:  # 迭代之
            if test_class == class_name:
                save_data_class = getattr(load_models, test_class)
                if save_data_class:
                    save_data_class.objects.all().delete()
                break

        abspath = os.path.abspath('.')
        with xlrd.open_workbook('./' + file_name) as data:
            print class_name + u"读取文件结束,开始导入!"
            table = data.sheet_by_index(0)  # 获取工作表
            rows_count = 1
            zero_numb = 0
            sql_save_list = []
            for line in range(rows_count, table.nrows):  # 行数 nrows = table.nrows
                row = table.row_values(line)  # 列数 table.row_values(rownum)
                if row:  # 查看行值是否为空
                    row = Databases_dataSave.foreachadd(check_rows, row)
                    sql_save_list.append(save_data_class().init1(row))
                else:
                    zero_numb = zero_numb + 1  # 空行值计数
                rows_count = rows_count + 1
                if rows_count % 999 == 0:
                    save_data_class.objects.bulk_create(sql_save_list)
                    sql_save_list = []

            print rows_count
            save_data_class.objects.bulk_create(sql_save_list)


    @classmethod
    def foreachadd(cls, list1, row):
        for nn in list1:
            if str(row[nn]).strip() == '':
                row[nn] = 0.0
        return row


class ScrapyDataAcquisition(AbstractDataAcquisition):
    def __init__(self):
        AbstractDataAcquisition.__init__(self)

    url_cell = "http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00805_dataList.action"
    para_dict_cell = {
        'export': "true",
        'key': str,
        'isHighWay': "0",
        'collectType': "1",
        'provinceId': "110",
        'cityId': "11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014",
        'districtId': "",
        'vendorId': "",
        'sysType': "",
        'lcName': "",
        'btsId': "",
        'localcell': "",
        'date': "2017-04-12",
        'flag': "normal",
        'start': "0",
        'limit': "25",
        'page': "1"
    }
    # rru小区爬取参数
    url_rru = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00862_dataList.action'
    para_dict_rru = {
        'export': 'true',
        'key': 'maintain_query_1492053585139',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'btsId': '',
        'flag': 'normal',
        'objectTypeId': 'L00862'
    }
    # 流量信息爬取参数
    url_traffic1 = 'http://10.245.0.91:10101/wonop/wonop/perf/exportDirect.action'
    para_dict_traffic1 = {
        'coutnerInfos': '[{"counterId":"LC0068050220376","lcName":"\u7a7a\u53e3\u4e0a\u884c\u4e1a\u52a1\u6d41\u91cf(MByte)","leaf":true,"checked":false,"statType":"\u516c\u5f0f"},{"counterId":"LC0068050220380","lcName":"\u7a7a\u53e3\u4e0b\u884c\u4e1a\u52a1\u6d41\u91cf(MByte)","leaf":true,"checked":false,"statType":"\u516c\u5f0f"}]',
        'levelId': 'L00805',
        'toLevelId': 'L00805',
        'netType': '4',
        'vendorId': '0',
        'timeRange': '{"period":"8","timeList":["2017-4-01 00:00:00","2017-4-02 00:00:00"]}',
        'toPeriod': '8',
        'neRange': '{"targetlevel":"cell","selecttype":"1","servicetype":"","neranges":[{"oids":"\'11001\'","lcnames":"\'\u5357\u5b81\'","level":"city","cityid":"11001"},{"oids":"\'11002\'","lcnames":"\'\u67f3\u5dde\'","level":"city","cityid":"11002"},{"oids":"\'11003\'","lcnames":"\'\u6842\u6797\'","level":"city","cityid":"11003"},{"oids":"\'11004\'","lcnames":"\'\u68a7\u5dde\'","level":"city","cityid":"11004"},{"oids":"\'11005\'","lcnames":"\'\u5317\u6d77\'","level":"city","cityid":"11005"},{"oids":"\'11006\'","lcnames":"\'\u9632\u57ce\u6e2f\'","level":"city","cityid":"11006"},{"oids":"\'11007\'","lcnames":"\'\u94a6\u5dde\'","level":"city","cityid":"11007"},{"oids":"\'11008\'","lcnames":"\'\u8d35\u6e2f\'","level":"city","cityid":"11008"},{"oids":"\'11009\'","lcnames":"\'\u7389\u6797\'","level":"city","cityid":"11009"},{"oids":"\'11010\'","lcnames":"\'\u767e\u8272\'","level":"city","cityid":"11010"},{"oids":"\'11011\'","lcnames":"\'\u8d3a\u5dde\'","level":"city","cityid":"11011"},{"oids":"\'11012\'","lcnames":"\'\u6cb3\u6c60\'","level":"city","cityid":"11012"},{"oids":"\'11013\'","lcnames":"\'\u6765\u5bbe\'","level":"city","cityid":"11013"},{"oids":"\'11014\'","lcnames":"\'\u5d07\u5de6\'","level":"city","cityid":"11014"},{"oids":"\'-1\'","lcnames":"\'\u5176\u5b83\'","level":"city","cityid":"-1"}],"checkedNodePaths":[["11001"],["11002"],["11003"],["11004"],["11005"],["11006"],["11007"],["11008"],["11009"],["11010"],["11011"],["11012"],["11013"],["11014"],["-1"]],"vendor":"0"}',
        'filterGroups': '[]',
        'sysTypes': '0',
        'provinceId': '110',
        'isBhFlag': '0',
        'busyFlag': '1',
        'selectType': '1',
        'sysType': '0'
    }
    # lte基站爬取参数
    url_enodeb = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00803_dataList.action'
    para_dict_enodeb = {
        'export': 'true',
        'key': 'maintain_query_1510215114654',
        'collectType': '1',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'vendorId': '',
        'siteType': '',
        'btsName': '',
        'btsId': '',
        'flag': 'normal',
        'isHighWay': '0',
        'objectTypeId': 'L00803'
    }
    # 物理站址爬取参数
    url_Phy_station = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00864_dataList.action'
    para_dict_Phys_station = {
        'export': 'true',
        'key': 'maintain_query_1510216622957',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'lcName': '',
        'flag': 'normal',
        'objectTypeId': 'L00864'
    }
    # 天线爬取参数
    url_antenna = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00863_dataList.action'
    para_dict_antenna = {
        'export': 'true',
        'key': 'maintain_query_1510216914611',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'antManuId': '',
        'flag': 'normal',
    }
    # bbu爬取参数
    url_bbu = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00861_dataList.action'
    para_dict_bbu = {
        'export': 'true',
        'key': 'maintain_query_1510216914611',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'btsName': '',
        'flag': 'normal',
        'objectTypeId': 'L00861',
    }
    # 小区场景爬取参数
    url_scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00903_dataList.action'
    para_dict_scenes = {
        'export': 'true',
        'key': 'maintain_query_1510217419212',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'districtId': '',
        'sysType': 'null',
        'scene1': '01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18',
        'scene2': '0101,0102,0103,0104,0201,0202,0203,0204,0301,0302,0303,0304,0305,0401,0402,0403,0501,0502,0503,0504,0505,0601,0602,0603,0701,0702,0703,0704,0801,0802,0803,0804,0806,0807,0808,0809,0810,0901,0902,0903,0904,0905,0906,0907,0908,1001,1002,1003,1101,1102,1103,1201,1202,1301,1401,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1601,1602,1603,1701,1801',
        'sceneName': '',
        'sceneID': '',
        'flag': 'normal',
        'objectTypeId': 'L00903',

    }
    url_cell2scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_CON02_dataListCon2.action'
    para_dict_cell2scenes = {
        'export': 'true',
        'key': 'maintain_query_1510218017331',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'netType': '',
        'scene1': '',
        'scene2': '',
        'sysType': 'null',
        'SCENE_ID': '',
        'sceneID': '',
        'CELL_ID': '',
        'CELL_NAME': '',
        'flag': 'normal',
        'queryType': '0',
        'objectTypeId': 'CON02',
    }
    # 网建场景爬取参数
    url_construction2scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_CON01_dataList.action'
    para_dict_construction2scenes = {
        'export': 'true',
        'key': 'maintain_query_1510218386472',
        'provinceId': '110',
        'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
        'scene1': '',
        'scene2': '',
        'sysType': 'null',
        'SCENE_ID': '',
        'sceneID': '',
        'CONSTRUCT_SCENE': '',
        'CONSTRUCT_GRIDTYPE': '',
        'CONTRUCT_GRIDNAME': '',
        'flag': 'normal',
        'queryType': '0',
        'objectTypeId': 'CON01',
    }
    # 删除数据爬取参数
    url_delete = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_property_delete_nocheck.action'
    para_dict_delete = {
        'objectTypeId': 'L00805',
        'objectIds': '110.703882.5',
        'selectedDelTypes': 'L00863,L00862,CON02'
        # selectedDelTypes: antenna->L00863,bbu->L00861,rru->L00862,PhysicallStation->L00864,cell2scenes->CON02,construction2scenes->CON03,

    }
    datestr = 'data'

    def scrapy_data(self):
        """爬取沃网络数据"""
        AbstractAsk.get_new_cookie()
        ask_lsit = [(oss_ask, self.url_rru, self.para_dict_rru, '%s/rru' % self.datestr),
                    (oss_ask, self.url_cell, self.para_dict_cell, '%s/cell' % self.datestr),
                    (oss_ask, self.url_enodeb, self.para_dict_enodeb, '%s/enodeb' % self.datestr),
                    (oss_ask, self.url_Phy_station, self.para_dict_Phys_station, '%s/physicalstation' % self.datestr),
                    (oss_ask, self.url_antenna, self.para_dict_antenna, '%s/antenna' % self.datestr),
                    (oss_ask, self.url_bbu, self.para_dict_bbu, '%s/bbu' % self.datestr),
                    (oss_ask, self.url_scenes, self.para_dict_scenes, '%s/scenes' % self.datestr),
                    (oss_ask, self.url_cell2scenes, self.para_dict_cell2scenes, '%s/cell2scenes' % self.datestr), ]
        try:
            for ask_example in ask_lsit:
                apply(gevent.spawn, ask_example).join()
            return True
        except:
            raise LookupError
        finally:
            end = time.clock()
            print str((end - start) / 60) + 'mins'

    def get_original_data(self):
        if self.scrapy_data():
            return True
        else:
            return False

    def delete_original_data(self):
        if os.path.exists('./' + self.datestr):
            shutil.rmtree('./' + self.datestr)
        return True


class DatabaseDataAcquisition(AbstractDataAcquisition):
    def get_original_data(self):
        pass

    def delete_original_data(self):
        pass

# Databases_dataSave().original_data_save()
