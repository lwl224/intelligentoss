import os
import unittest

from tool import scrapy
from tool import oss_data_treating


import django
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intelligentoss.settings")
    django.setup()


# class Testscrapy(unittest.TestCase):
#     def test_init(self):
#         pass
#
#     # self.assertTrue(scrapy.get_new_cookie())
#
#     def test_getexcel(self):
#         datestr = 'data'
#         url_cell = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00805_dataList.action'
#         para_dict_cell = {
#             'export': "true",
#             'key': str,
#             'isHighWay': "0",
#             'collectType': "1",
#             'provinceId': "110",
#             'cityId': "11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014",
#             'districtId': "",
#             'vendorId': "",
#             'sysType': "",
#             'lcName': "",
#             'btsId': "",
#             'localcell': "",
#             'date': "2017-04-12",
#             'flag': "normal",
#             'start': "0",
#             'limit': "25",
#             'page': "1"
#         }
#         self.assertTrue(scrapy.oss_ask(url_cell, para_dict_cell, '%s/cell' % datestr))
#
#     def test_getexcel1(self):
#         url_delete = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_property_delete_nocheck.action'
#         para_dict_delete = {
#             'objectTypeId': 'L00805',
#             'objectIds': '110.703882.5',
#             'selectedDelTypes': 'L00863,L00862,CON02'
#             # selectedDelTypes: antenna->L00863,bbu->L00861,rru->L00862,PhysicallStation->L00864,cell2scenes->CON02,construction2scenes->CON03,
#         }
#         self.assertEquals(scrapy.oss_ask(url_delete, para_dict_delete, '%s/cell' % 'data'), )
#
#         # def test_key(self):
#         #     d = Dict()
#         #     d['key'] = 'value'
#         #     self.assertEquals(d.key, 'value')
#         #
#         # def test_attr(self):
#         #     d = Dict()
#         #     d.key = 'value'
#         #     self.assertTrue('key' in d)
#         #     self.assertEquals(d['key'], 'value')
#         #
#         # def test_keyerror(self):
#         #     d = Dict()
#         #     with self.assertRaises(KeyError):
#         #         value = d['empty']
#         #
#         # def test_attrerror(self):
#         #     d = Dict()
#         #     with self.assertRaises(AttributeError):
#         #         value = d.empty

class Tests_oss_treating(unittest.TestCase):
    def test_init(self):
        pass

    # def test_get_original_data(self):
    #     self.assertTrue(oss_data_treating.ScrapyDataAcquisition().get_original_data())

    # def test_delete_original_data(self):
    #     self.assertTrue(oss_data_treating.ScrapyDataAcquisition().delete_original_data())

    def test_delete_original_data(self):
        self.assertTrue(oss_data_treating.Databases_dataSave().original_data_save())


if __name__ == '__main__':
    unittest.main()
