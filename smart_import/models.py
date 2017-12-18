# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from tool.scrapy import *

CITYID = {"南宁市": "11001",
          "柳州市": "11002",
          "桂林市": "11003",
          "梧州市": "11004",
          "北海市": "11005",
          "防城港市": "11006",
          "钦州市": "11007",
          "贵港市": "11008",
          "玉林市": "11009",
          "百色市": "11010",
          "贺州市": "11011",
          "河池市": "11012",
          "来宾市": "11013",
          "崇左市": "11014", }
DISTRICT_ID = {
    "兴宁区": "1100102",
    "青秀区": "1100103",
    "江南区": "1100105",
    "西乡塘区": "1100107",
    "良庆区": "1100108",
    "邕宁区": "1100109",
    "武鸣县": "1100122",
    "隆安县": "1100123",
    "马山县": "1100124",
    "上林县": "1100125",
    "宾阳县": "1100126",
    "横县": "1100127",
    "城中区": "1100202", "鱼峰区": "1100203", "柳南区": "1100204", "柳北区": "1100205", "柳江县": "1100221", "柳城县": "1100222",
    "鹿寨县": "1100223", "融安县": "1100224", "融水苗族自治县": "1100225", "三江侗族自治县": "1100226", "秀峰区": "1100302",
    "叠彩区": "1100303", "象山区": "1100304", "七星区": "1100305", "雁山区": "1100311", "阳朔县": "1100321", "临桂县": "1100322",
    "灵川县": "1100323", "全州县": "1100324", "兴安县": "1100325", "永福县": "1100326", "灌阳县": "1100327",
    "龙胜各族自治县": "1100328", "资源县": "1100329", "平乐县": "1100330", "荔浦县": "1100331", "恭城瑶族自治县": "1100332",
    "万秀区": "1100403", "蝶山区": "1100404", "长洲区": "1100405", "苍梧县": "1100421", "藤县": "1100422", "蒙山县": "1100423",
    "岑溪市": "1100481", "海城区": "1100502", "银海区": "1100503", "铁山港区": "1100512", "合浦县": "1100521", "港口区": "1100602",
    "防城区": "1100603", "上思县": "1100621", "东兴市": "1100681", "钦南区": "1100702", "钦北区": "1100703", "灵山县": "1100721",
    "浦北县": "1100722", "港北区": "1100802", "港南区": "1100803", "覃塘区": "1100804", "平南县": "1100821", "桂平市": "1100881",
    "玉州区": "1100902", "容县": "1100921", "陆川县": "1100922", "博白县": "1100923", "兴业县": "1100924", "北流市": "1100981",
    "右江区": "1101002", "田阳县": "1101021", "田东县": "1101022", "平果县": "1101023", "德保县": "1101024", "靖西县": "1101025",
    "那坡县": "1101026", "凌云县": "1101027", "乐业县": "1101028", "田林县": "1101029", "西林县": "1101030",
    "隆林各族自治县": "1101031", "八步区": "1101102", "昭平县": "1101121", "钟山县": "1101122", "富川瑶族自治县": "1101123",
    "平桂区": "1101124", "金城江区": "1101202", "南丹县": "1101221", "天峨县": "1101222", "凤山县": "1101223", "东兰县": "1101224",
    "罗城仫佬族自治县": "1101225", "环江毛南族自治县": "1101226", "巴马瑶族自治县": "1101227", "都安瑶族自治县": "1101228",
    "大化瑶族自治县": "1101229", "宜州市": "1101281", "兴宾区": "1101302", "忻城县": "1101321", "象州县": "1101322",
    "武宣县": "1101323", "金秀瑶族自治县": "1101324", "合山市": "1101381", "江洲区": "1101402", "扶绥县": "1101421",
    "宁明县": "1101422", "龙州县": "1101423", "大新县": "1101424", "天等县": "1101425", "凭祥市": "1101481"}
ADMIN_REGIONSlist = {"城区": "1",
                     "县城": "2",
                     "乡镇": "3",
                     "其他": "9",
                     }
IS_Mrlist = {"未采集": "0",
             "已采集": "1",
             }
DUP_MODElist = {"FDD": "0",
                "TDD": "1",
                }
RRUCELL_FLAGlist = {"不是射频拉远的小区": "0",
                    "射频拉远的小区": "1",
                    }
COVER_TYPElist = {"室外": "1",
                  "室内": "2",
                  "室内拖室外": "3",
                  "室外拖室内": "4",
                  }
Ifnotlist = {"是": "1",
             "否": "0",
             }
CELL_ACTIVE_STATElist = {"激活": "1",
                         "去激活": "2",
                         }
HIGH_SPEED_FLAGlist = {"高速小区": "1",
                       "低速小区": "2",
                       }
CSFBlist = {"GSM": "1",
            "WCDMA": "2",
            }
COMPANYlist = {"电信": "1",
               "联通": "2",
               }
SHARED_TYPElsit = {"独立载频": "1",
                   "共享载频": "2",
                   }
VENDOR_Idlsit = {"华为": "1",
                 "中兴": "2",
                 "诺基亚": "5",
                 }
TX_RX_MODElist = {
    "1T1R(一发一收)": "1",
    "1T2R(一发二收)": "2",
    "2T2R(两发两收)": "3",
    "2T4R(两发四收)": "4",
    "4T4R(四发四收)": "5",
    "8T8R(八发八收)": "6",

}
RRU_MODELlist = {"RRU": "1",
                 "载频板": "2",
                 }


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)


class Antenna(models.Model):
    antennaid = models.CharField(max_length=512)
    antennaid1 = models.CharField(max_length=512)
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    district = models.CharField(max_length=512)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    physicalstationid = models.CharField(max_length=512)
    rruid = models.CharField(max_length=512)
    cellid1 = models.CharField(max_length=512)
    directionangle = models.FloatField(blank=True, null=True)
    antennaheight = models.FloatField(blank=True, null=True)
    electricaldowntilt = models.CharField(max_length=512)
    mechanicaltilt = models.CharField(max_length=512)
    antennatypes = models.CharField(max_length=512)
    beautifytypes = models.CharField(max_length=512)
    antennafactory = models.CharField(max_length=512)
    antennamodel = models.CharField(max_length=512)
    antennanum = models.CharField(max_length=512)
    horizontalpowerangle = models.CharField(max_length=512)
    verticalpowerangle = models.CharField(max_length=512)
    antennagain = models.CharField(max_length=512)
    picture1 = models.CharField(max_length=512)
    picture2 = models.CharField(max_length=512)
    picture3 = models.CharField(max_length=512)
    picture4 = models.CharField(max_length=512)
    towermast = models.CharField(max_length=512)
    txrxmod = models.CharField(max_length=512)
    verticalrange = models.CharField(max_length=512)
    install = models.CharField(max_length=512)

    def init1(self, *args):
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.antennaid = args[0]
                self.antennaid1 = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.lon = args[5]
                self.lat = args[6]
                self.physicalstationid = args[7]
                self.rruid = args[8]
                self.cellid1 = args[9]
                self.directionangle = args[10]
                self.antennaheight = args[11]
                self.electricaldowntilt = args[12]
                self.mechanicaltilt = args[13]
                self.antennatypes = args[14]
                self.beautifytypes = args[15]
                self.antennafactory = args[16]
                self.antennamodel = args[17]
                self.antennanum = args[18]
                self.horizontalpowerangle = args[19]
                self.verticalpowerangle = args[20]
                self.antennagain = args[21]
                self.picture1 = args[22]
                self.picture2 = args[23]
                self.picture3 = args[24]
                self.picture4 = args[25]
                self.towermast = args[26]
                self.txrxmod = args[27]
                self.verticalrange = args[28]
                self.install = args[29]
        return self

    def makeDataToOss(self):
        para_dict = {
            'timestamp': '1512009575000',
            'objectTypeId': 'L00863',
            'objectId': 'null',
            'complaintId': 'null',
            'cell_4g': '',
            'cell_3g': '',
            'cell_2g': '',
            'test': '',
            'ANT_ID': self.antennaid,
            'NMS_ORIG_RES_NAME': self.antennaid1,
            'PROVINCE_ID': '110',
            'CITY_ID': CITYID[self.city],
            'DISTRICT_ID': DISTRICT_ID[self.district],
            'LONGITUDE': self.lon,
            'LATITUDE': self.lat,
            'PHY_ID': self.physicalstationid,
            'RELATED_RRU': self.rruid,
            'RELATED_CELL': self.cellid1,
            'ANT_AZIMUTH': self.directionangle,
            'ANT_HIGH': self.antennaheight,
            'ANT_ELECTANGLE': self.electricaldowntilt,
            'ANT_MACHANGLE': self.mechanicaltilt,
            'ANT_TYPE': '2',
            'BEA_TYPE': '2',
            'ANT_EQUIP': self.antennafactory,
            'ANT_EQUIPMODULE': self.antennamodel,
            'PORT_NUM': self.antennanum,
            'LEVEL_POWER': self.horizontalpowerangle,
            'APEAK_POWER': self.verticalpowerangle,
            'ANT_GAIN': self.antennagain,
            'ATTACH_ENT': self.picture1,
            'ATTACH_COV': self.picture2,
            'ATTACH_PHY': self.picture3,
            'ATTACH_QUE': self.picture4,
            'TOWER_TYPE': '3',
            'TX_RX_MODE': TX_RX_MODElist[self.txrxmod],
            'VERTICAL_DIST': self.verticalrange,
            'PHY_TYPE': '',

        }
        try:
            AbstractAsk.get_new_cookie()
            modify_url = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_modify_nocheck.action'
            respond_msg = oss_ask(modify_url, para_dict, None, AskModify)
            if respond_msg == 'true':
                self.save()
        except:
            raise ValueError('input error!')


class Cell2scenes(models.Model):
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    scenesid = models.CharField(max_length=512)
    cellid1 = models.CharField(max_length=512)
    networktype = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Cell2scenes, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.province = args[0]
                self.city = args[1]
                self.scenesid = args[2]
                self.cellid1 = args[3]
                self.networktype = args[4]
        return self

    def makeDataToOss(self):
        modify_url = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_add_nocheckEx.action'
        para_dict = {
            'timestamp': '1512011210000',
            'objectTypeId': 'CON02',
            'complaintId': 'null',
            'objectId': 'null',
            'batchValue': '',
            'test': '',
            'PROVINCE_ID': '110',
            'CITY_ID': CITYID[self.city],
            'OID': self.scenesid,
            'RELATED_CELL_OID': self.cellid1,
            'NET_TYPE': '4',
        }
        try:
            AbstractAsk.get_new_cookie()
            respond_msg = oss_ask(modify_url, para_dict, None, AskModify)
            if respond_msg == 'true':
                self.save()
        except:
            raise ValueError('input error!')


class Enodeb(models.Model):
    physicalstationnumb23g = models.CharField(max_length=512)
    sourcetypes = models.CharField(max_length=512)
    commonmode = models.CharField(max_length=512)
    unittype = models.CharField(max_length=512)
    hwversion = models.CharField(max_length=512)
    swversion = models.CharField(max_length=512)
    swbugversion = models.CharField(max_length=512)
    s1ubandwidth = models.CharField(max_length=512)
    enodebbandwidth1 = models.CharField(max_length=512)
    enodebbandwidth2 = models.CharField(max_length=512)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    Carrier = models.CharField(max_length=512)
    Sectortype = models.CharField(max_length=512)
    bbunumb = models.CharField(max_length=512)
    rrunumb = models.CharField(max_length=512)
    rrunumb24G = models.CharField(max_length=512)
    repeater = models.CharField(max_length=512)
    bstype = models.CharField(max_length=512)
    location = models.CharField(max_length=512)
    bslevel = models.CharField(max_length=512)
    mcc = models.CharField(max_length=512)
    mnc = models.CharField(max_length=512)
    enodebcell = models.CharField(max_length=512)
    enodebip = models.CharField(max_length=512)
    towerdelivery = models.CharField(max_length=512)
    towerlocation = models.CharField(max_length=512)
    towerlevel = models.CharField(max_length=512)
    sharetelecom = models.CharField(max_length=512)
    builder = models.CharField(max_length=512)
    share = models.CharField(max_length=512)
    sharebs = models.CharField(max_length=512)
    customize1 = models.CharField(max_length=512)
    customize2 = models.CharField(max_length=512)
    customize3 = models.CharField(max_length=512)
    customize4 = models.CharField(max_length=512)
    customize5 = models.CharField(max_length=512)
    customize6 = models.CharField(max_length=512)
    customize7 = models.CharField(max_length=512)
    customize8 = models.CharField(max_length=512)
    customize9 = models.CharField(max_length=512)
    customize10 = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Enodeb, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.enodebname = args[0]
                self.enodebomcidentify = args[1]
                self.enodebomcname = args[2]
                self.province = args[3]
                self.city = args[4]
                self.district = args[5]
                self.villages = args[6]
                self.enodebid = args[7]
                self.enodebid2 = args[8]
                self.enodebid3 = args[9]
                self.enodebdn = args[10]
                self.emsid = args[11]
                self.mmeid = args[12]
                self.sgwid = args[13]
                self.factory = args[14]
                self.worktypes = args[15]
                self.updatatime = args[16]
                self.antennanumb = args[17]
                self.antennanumb2g = args[18]
                self.antennanumb3g = args[19]
                self.antennanumb23g = args[20]
                self.physicalstationnumb = args[21]
                self.physicalstationnumb2g = args[22]
                self.physicalstationnumb3g = args[23]
                self.physicalstationnumb23g = args[24]
                self.sourcetypes = args[25]
                self.commonmode = args[26]
                self.unittype = args[27]
                self.hwversion = args[28]
                self.swversion = args[29]
                self.swbugversion = args[30]
                self.s1ubandwidth = args[31]
                self.enodebbandwidth1 = args[32]
                self.enodebbandwidth2 = args[33]
                self.lon = args[34]
                self.lat = args[35]
                self.Carrier = args[36]
                self.Sectortype = args[37]
                self.bbunumb = args[38]
                self.rrunumb = args[39]
                self.rrunumb24G = args[40]
                self.repeater = args[41]
                self.bstype = args[42]
                self.location = args[43]
                self.bslevel = args[44]
                self.mcc = args[45]
                self.mnc = args[46]
                self.enodebcell = args[47]
                self.enodebip = args[48]
                self.towerdelivery = args[49]
                self.towerlocation = args[50]
                self.towerlevel = args[51]
                self.sharetelecom = args[52]
                self.builder = args[53]
                self.share = args[54]
                self.sharebs = args[55]
                self.customize1 = args[56]
                self.customize2 = args[57]
                self.customize3 = args[58]
                self.customize4 = args[59]
                self.customize5 = args[60]
                self.customize6 = args[61]
                self.customize7 = args[62]
                self.customize8 = args[63]
                self.customize9 = args[64]
                self.customize10 = args[65]

        return self


class Rru(models.Model):
    rruid = models.CharField(max_length=512)
    rruname = models.CharField(max_length=512)
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    district = models.CharField(max_length=512)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    bbuid = models.CharField(max_length=512)
    cellid1 = models.CharField(max_length=512)
    physicalstationid = models.CharField(max_length=512)
    rrutypes = models.CharField(max_length=512)
    rruport = models.CharField(max_length=512)
    txrxtypes = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Rru, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.rruid = args[0]
                self.rruname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.lon = args[5]
                self.lat = args[6]
                self.bbuid = args[7]
                self.cellid1 = args[8]
                self.physicalstationid = args[9]
                self.rrutypes = args[10]
                self.rruport = args[11]
                self.txrxtypes = args[12]
        return self

    def makeDataToOss(self):
        modify_url = ' http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_add_nocheck.action'
        para_dict = {
            'timestamp': '1512005842000',
            'objectTypeId': 'L00862',
            'complaintId': 'null',
            'objectId': 'null',
            'cell_4g': '',
            'cell_3g': '',
            'cell_2g': '',
            'test': '',
            'RRU_ID': self.rruid,
            'LC_NAME': self.rruname,
            'PROVINCE_ID': '110',
            'CITY_ID': CITYID[self.city],
            'DISTRICT_ID': DISTRICT_ID[self.district],
            'LONGITUDE': self.lon,
            'LATITUDE': self.lat,
            'RELATED_BBU_ID': self.bbuid,
            'RELATED_CELL': self.cellid1,
            'PHY_ID': self.physicalstationid,
            'RRU_MODEL': RRU_MODELlist[self.rrutypes],
            'RRU_PORT': self.rruport,
            'TX_RX_MODE': TX_RX_MODElist[self.txrxtypes],

        }
        try:
            AbstractAsk.get_new_cookie()
            respond_msg = oss_ask(modify_url, para_dict, None, AskModify)
            if respond_msg == 'true':
                self.save()
        except:
            raise ValueError('input error!')


class Bbu(models.Model):
    bbuid = models.CharField(max_length=512)
    bbuname = models.CharField(max_length=512)
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    district = models.CharField(max_length=512)
    factory = models.CharField(max_length=512)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    enodebid3 = models.CharField(max_length=512)
    physicalstationid = models.CharField(max_length=512)
    unittype = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Bbu, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.bbuid = args[0]
                self.bbuname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.factory = args[5]
                self.lon = args[6]
                self.lat = args[7]
                self.enodebid3 = args[8]
                self.physicalstationid = args[9]
                self.unittype = args[10]
        return self


class Physicalstation(models.Model):
    physicalstationid = models.CharField(max_length=512)
    physicalstationname = models.CharField(max_length=512)
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    district = models.CharField(max_length=512)
    fulladdress = models.CharField(max_length=512)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    altitude = models.CharField(max_length=512)
    isboundary = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.physicalstationid = args[0]
                self.physicalstationname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.fulladdress = args[5]
                self.lon = args[6]
                self.lat = args[7]
                self.altitude = args[8]
                self.isboundary = args[9]
        return self


class exceldata(models.Model):
    username = models.CharField(max_length=30)
    headImg = models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.username


class Scenes(models.Model):
    province = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    district = models.CharField(max_length=512)
    scenesid = models.CharField(max_length=512)
    scenesname = models.CharField(max_length=512)
    parentscenes = models.CharField(max_length=512)
    scenesdescription = models.CharField(max_length=3000)
    scenesrange = models.CharField(max_length=3000)
    sceneslon = models.FloatField(blank=True, null=True)
    sceneslat = models.FloatField(blank=True, null=True)
    firstscenes = models.CharField(max_length=512)
    secondscenes = models.CharField(max_length=512)
    hotregion = models.CharField(max_length=512)
    vitalarea = models.CharField(max_length=512)
    population = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    cell2g = models.CharField(max_length=512)
    cell3g = models.CharField(max_length=512)
    cell4g = models.CharField(max_length=512)
    carrier2g = models.CharField(max_length=512)
    carrier3g = models.CharField(max_length=512)
    carrier4g = models.CharField(max_length=512)
    fpoint2g = models.CharField(max_length=512)
    fpoint3g = models.CharField(max_length=512)
    fpoint4g = models.CharField(max_length=512)
    mobilecover2g = models.CharField(max_length=512)
    mobilecover3g = models.CharField(max_length=512)
    mobilecover4g = models.CharField(max_length=512)
    mobilefpoint = models.CharField(max_length=512)
    telecomcover2g = models.CharField(max_length=512)
    telecomcover3g = models.CharField(max_length=512)
    telecomcover4g = models.CharField(max_length=512)
    telecomfpoint = models.CharField(max_length=512)
    sceneslevel = models.CharField(max_length=512)
    customize1 = models.CharField(max_length=512)
    customize2 = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Scenes, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.province = args[0]
                self.city = args[1]
                self.district = args[2]
                self.scenesid = args[3]
                self.scenesname = args[4]
                self.parentscenes = args[5]
                self.scenesdescription = args[6]
                self.scenesrange = args[7]
                self.sceneslon = args[8]
                self.sceneslat = args[9]
                self.firstscenes = args[10]
                self.secondscenes = args[11]
                self.hotregion = args[12]
                self.vitalarea = args[13]
                self.population = args[14]
                self.area = args[15]
                self.cell2g = args[16]
                self.cell3g = args[17]
                self.cell4g = args[18]
                self.carrier2g = args[19]
                self.carrier3g = args[20]
                self.carrier4g = args[21]
                self.fpoint2g = args[22]
                self.fpoint3g = args[23]
                self.fpoint4g = args[24]
                self.mobilecover2g = args[25]
                self.mobilecover3g = args[26]
                self.mobilecover4g = args[27]
                self.mobilefpoint = args[28]
                self.telecomcover2g = args[29]
                self.telecomcover3g = args[30]
                self.telecomcover4g = args[31]
                self.telecomfpoint = args[32]
                self.sceneslevel = args[33]
                self.customize1 = args[34]
                self.customize2 = args[35]
        return self





class Wcdmacell(models.Model):
    cellname = models.CharField(max_length=512)
    lac = models.CharField(max_length=512)
    ci = models.CharField(max_length=512)
    nodebname = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    totalstations = models.CharField(max_length=512)
    physicalstationname = models.CharField(max_length=512)
    physicalstationid = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[0]
                lac1 = str(int(args[1]))
                ci1 = str(int(args[2]))
                self.lac = lac1
                self.ci = ci1
                self.nodebname = args[3]
                self.city = args[4] + u'市'
                self.totalstations = args[9]
                self.physicalstationname = args[10]
                self.physicalstationid = args[11]
        return self


class Gsmcell(models.Model):
    cellname = models.CharField(max_length=512)
    lac = models.CharField(max_length=512)
    ci = models.CharField(max_length=512)
    nodebname = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    totalstations = models.CharField(max_length=512)
    physicalstationname = models.CharField(max_length=512)
    physicalstationid = models.CharField(max_length=512)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[10]
                lac1 = str(int(args[11]))
                ci1 = str(int(args[12]))
                self.lac = lac1
                self.ci = ci1
                self.nodebname = args[7]
                self.city = args[1] + u'市'
                self.totalstations = args[60]
                self.physicalstationname = args[65]
                self.physicalstationid = args[66]
        return self


class Ltecell(models.Model):
    cellname = models.CharField(max_length=256)
    cellid1 = models.CharField(max_length=256)
    cellomcname = models.CharField(max_length=256)
    province = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    villages = models.CharField(max_length=256)
    enodebid = models.CharField(max_length=256)
    cellid2 = models.CharField(max_length=256)
    sector = models.CharField(max_length=256)
    eutranCellid = models.CharField(max_length=256)
    factory = models.CharField(max_length=256)
    villagestypes = models.CharField(max_length=256)
    MR = models.CharField(max_length=256)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    antennaid = models.CharField(max_length=256)
    antennanum = models.CharField(max_length=256)
    worktypes = models.CharField(max_length=256)
    cp = models.CharField(max_length=256)
    subframe = models.CharField(max_length=256)
    specificsubframe = models.CharField(max_length=256)
    remoterru = models.CharField(max_length=256)
    upfpoint = models.CharField(max_length=256)
    downfpoint = models.CharField(max_length=256)
    pci = models.CharField(max_length=256)
    pcilist = models.CharField(max_length=256)
    cellmaxpower = models.CharField(max_length=256)
    rspower = models.CharField(max_length=256)
    atypepower1 = models.CharField(max_length=256)
    btypepower1 = models.CharField(max_length=256)
    atypepower2 = models.CharField(max_length=256)
    btypepower2 = models.CharField(max_length=256)
    bcchpower = models.CharField(max_length=256)
    maxpower = models.CharField(max_length=256)
    tac = models.CharField(max_length=256)
    taclist = models.CharField(max_length=256)
    operation = models.CharField(max_length=256)
    updatatime = models.CharField(max_length=256)
    coveragetypes = models.CharField(max_length=256)
    coveragerange = models.CharField(max_length=256)
    plmn = models.CharField(max_length=256)
    mbms = models.CharField(max_length=256)
    band = models.CharField(max_length=256)
    centerfrequency = models.CharField(max_length=256)
    bandwidth = models.CharField(max_length=256)
    downCyclicPrefix = models.CharField(max_length=256)
    upCyclicPrefix = models.CharField(max_length=256)
    upbandwidth = models.CharField(max_length=256)
    downbandwidth = models.CharField(max_length=256)
    astat = models.CharField(max_length=256)
    hs = models.CharField(max_length=256)
    txrxmod = models.CharField(max_length=256)
    worktypes1 = models.CharField(max_length=256)
    leadingformat = models.CharField(max_length=256)
    isblocking = models.CharField(max_length=256)
    boundarycell = models.CharField(max_length=256)
    boundaryname = models.CharField(max_length=256)
    csbf = models.CharField(max_length=256)
    hs2 = models.CharField(max_length=256)
    istelecom = models.CharField(max_length=256)
    build = models.CharField(max_length=256)
    sharingmode = models.CharField(max_length=256)
    isca = models.CharField(max_length=256)
    catypes = models.CharField(max_length=256)
    catypeassociation = models.CharField(max_length=256)
    camaincellid = models.CharField(max_length=256)
    customize1 = models.CharField(max_length=256)
    customize2 = models.CharField(max_length=256)
    customize3 = models.CharField(max_length=256)
    customize4 = models.CharField(max_length=256)
    customize5 = models.CharField(max_length=256)
    customize6 = models.CharField(max_length=256)
    customize7 = models.CharField(max_length=256)
    customize8 = models.CharField(max_length=256)
    customize9 = models.CharField(max_length=256)
    customize10 = models.CharField(max_length=256)

    def init1(self, *args):
        # super(Ltecell, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[0]
                self.cellid1 = args[1]
                self.cellomcname = args[2]
                self.province = args[3]
                self.city = args[4]
                self.district = args[5]
                self.villages = args[6]
                self.enodebid = args[7]
                self.cellid2 = args[8]
                self.sector = args[9]
                self.eutranCellid = args[10]
                self.factory = args[11]
                self.villagestypes = args[12]
                self.MR = args[13]
                self.lon = args[14]
                self.lat = args[15]
                self.antennaid = args[16]
                self.antennanum = args[17]
                self.worktypes = args[18]
                self.cp = args[19]
                self.subframe = args[20]
                self.specificsubframe = args[21]
                self.remoterru = args[22]
                self.upfpoint = args[23]
                self.downfpoint = args[24]
                self.pci = args[25]
                self.pcilist = args[26]
                self.cellmaxpower = args[27]
                self.rspower = args[28]
                self.atypepower1 = args[29]
                self.btypepower1 = args[30]
                self.atypepower2 = args[31]
                self.btypepower2 = args[32]
                self.bcchpower = args[33]
                self.maxpower = args[34]
                self.tac = args[35]
                self.taclist = args[36]
                self.operation = args[37]
                self.updatatime = args[38]
                self.coveragetypes = args[39]
                self.coveragerange = args[40]
                self.plmn = args[41]
                self.mbms = args[42]
                self.band = args[43]
                self.centerfrequency = args[44]
                self.bandwidth = args[45]
                self.downCyclicPrefix = args[46]
                self.upCyclicPrefix = args[47]
                self.upbandwidth = args[48]
                self.downbandwidth = args[49]
                self.astat = args[50]
                self.hs = args[51]
                self.txrxmod = args[52]
                self.worktypes1 = args[53]
                self.leadingformat = args[54]
                self.isblocking = args[55]
                self.boundarycell = args[56]
                self.boundaryname = args[57]
                self.csbf = args[58]
                self.hs2 = args[59]
                self.istelecom = args[60]
                self.build = args[61]
                self.sharingmode = args[62]
                self.isca = args[63]
                self.catypes = args[64]
                self.catypeassociation = args[65]
                self.camaincellid = args[66]
                self.customize1 = args[67]
                self.customize2 = args[68]
                self.customize3 = args[69]
                self.customize4 = args[70]
                self.customize5 = args[71]
                self.customize6 = args[72]
                self.customize7 = args[73]
                self.customize8 = args[74]
                self.customize9 = args[75]
                self.customize10 = args[76]

        return self

    def syn1(self):
        synrru = Rru.objects.filter(cellid1=self.cellid1)[0]
        para_dict = {'timestamp': '1511059747000', 'objectTypeId': 'L00862', 'complaintId': 'null',
                     'objectId': '110.' + synrru.rruid, 'cell_4g': '', 'cell_3g': '', 'cell_2g': '', 'test': '',
                     'RRU_ID': synrru.rruid, 'LC_NAME': synrru.rruname, 'PROVINCE_ID': '110', 'CITY_ID': '11001',
                     'DISTRICT_ID': '1100126', 'LONGITUDE': '108.855926', 'LATITUDE': '23.236786',
                     'RELATED_BBU_ID': synrru.bbuid, 'RELATED_CELL': synrru.cellid1,
                     'PHY_ID': synrru.physicalstationid,
                     'RRU_MODEL': '1', 'RRU_PORT': synrru.rruport, 'TX_RX_MODE': '3'}
        para_dict['CITY_ID'] = CITYID[self.city]
        para_dict['DISTRICT_ID'] = DISTRICT_ID[self.district]
        para_dict['LONGITUDE'] = self.lon
        para_dict['LATITUDE'] = self.lat
        synrru.city = self.city
        synrru.district = self.district
        synrru.lon = self.lon
        synrru.lat = self.lat

        try:
            AbstractAsk.get_new_cookie()
            modify_url = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_modify_nocheck.action'
            respond_msg = oss_ask(modify_url, para_dict, None, AskModify)
            if respond_msg == 'true':
                synrru.save()
        except:
            raise ValueError('input error!')

    def makeDataToOss(self):

        modify_url = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_add_nocheckEx.action'
        para_dict = {
            'timestamp': '1511754782000',
            'objectTypeId': 'L00805',
            'complaintId': 'null',
            'objectId': 'null',
            'batchValue': '',
            'test': '',
            'LC_NAME': self.cellname,
            'EMS_ORIG_RES_ID': self.cellid1,
            'EMS_ORIG_RES_NAME': self.cellomcname,
            'PROVINCE_ID': '110',
            'CITY_ID': CITYID[self.city],
            'DISTRICT_ID': DISTRICT_ID[self.district],
            'TOWN_ID': self.villages,
            'ENODEB_ID': self.enodebid,
            'CELL_ID': self.cellid2,
            'RELATED_SECTOR_ID': self.sector,
            'VENDOR_CELL_ID': self.eutranCellid,
            'VENDOR_ID': VENDOR_Idlsit[self.factory],
            'ADMIN_REGIONS': ADMIN_REGIONSlist[self.villagestypes],
            'IS_MR': IS_Mrlist[self.MR],
            'LONGITUDE': self.lon,
            'LATITUDE': self.lat,
            'RELATED_ANTENNA_LIST': self.antennaid,
            'ANT_NUM': self.antennanum,
            'DUP_MODE': DUP_MODElist[self.worktypes],
            'CP_TYPE': '0',
            'SUB_FRAME_TYPE': '7',
            'SPE_SUB_FRAME_TYPE': '9',
            'RRUCELL_FLAG': RRUCELL_FLAGlist[self.remoterru],
            'UPLINK_FREQ': self.upfpoint,
            'DOWNLINK_FREQ': self.downfpoint,
            'PHYSIC_CELL_ID': self.pci,
            'PCI_LIST': self.pcilist,
            'MAX_TRANSMIT_POWER': self.cellmaxpower,
            'RS_EPRE': self.rspower,
            'RHO_A': self.atypepower1,
            'RHO_B': self.btypepower1,
            'PA': self.atypepower2,
            'PB': self.btypepower2,
            'BCH_POWER': self.bcchpower,
            'MAXIMUM_TRANSMISSION_POWER': self.maxpower,
            'TRACE_AREA_CODE': self.tac,
            'TRACE_AREA_LIST': self.taclist,
            'WORK_STATE': '2',
            'COVER_TYPE': COVER_TYPElist[self.coveragetypes],
            'CELL_SIZE': self.coveragerange,
            'PLMN_ID_LIST': self.plmn,
            'CELL_MBMS_SWITCH': Ifnotlist[self.mbms],
            'BAND_INDICATOR': self.band,
            'EARFCN': self.centerfrequency,
            'BAND_WIDTH': self.bandwidth,
            'DL_CYCLIC_PREFIX': self.downCyclicPrefix,
            'UL_CYCLIC_PREFIX': self.upCyclicPrefix,
            'UL_BAND_WIDTH': self.upbandwidth,
            'DL_BAND_WIDTH': self.downbandwidth,
            'CELL_ACTIVE_STATE': CELL_ACTIVE_STATElist[self.astat],
            'HIGH_SPEED_FLAG': HIGH_SPEED_FLAGlist[self.hs],
            'TX_RX_MODE': self.txrxmod,
            'WORK_MODE': '1',
            'PREAMBLE_FMT': self.leadingformat,
            'CELL_ADMIN_STATE': Ifnotlist[self.isblocking],
            'IS_BOUNDARY': Ifnotlist[self.boundarycell],
            'ADJACENT_PRO': self.boundaryname,
            'CSFB': CSFBlist[self.csbf],
            'IS_SECOND': Ifnotlist[self.hs2],
            'IS_SHARED': Ifnotlist[self.istelecom],
            'COMPANY': COMPANYlist[self.build],
            'SHARED_TYPE': SHARED_TYPElsit[self.sharingmode],
            'IS_AGGRE': Ifnotlist[self.isca],
            'AGGRE_TYPE': '0',
            'FREQ_TYPE': '7',
            'PCELL_ID': self.camaincellid,
            'RESERVED1': self.customize1,
            'RESERVED2': self.customize2,
            'RESERVED3': self.customize3,
            'RESERVED4': self.customize4,
            'RESERVED5': self.customize5,
            'RESERVED6': self.customize6,
            'RESERVED7': self.customize7,
            'RESERVED8': self.customize8,
            'RESERVED9': self.customize9,
            'RESERVED10': self.customize10,
        }
        try:
            AbstractAsk.get_new_cookie()
            respond_msg = oss_ask(modify_url, para_dict, None, AskModify)
            if respond_msg == 'true':
                self.save()
        except:
            raise ValueError('input error!')



class Cellunion(models.Model):
    cell = Ltecell()
    rru = Rru()
    ant = Antenna
    scenes = Scenes()

    def init1(self, *args):
        if args:
            if type(args[0]) is list:
                args = args[0]
                self.cell = Ltecell().init1(args[0:77])
                rruargs = args[77:79]
                rruargs.extend(args[3:6])
                rruargs.extend(args[14:16])
                rruargs.append(args[79])
                rruargs.append(args[1])
                rruargs.extend(args[80:84])
                self.rru = Rru().init1(rruargs)
                antargs = args[84:86]
                antargs.extend(args[3:6])
                antargs.extend(args[14:16])
                antargs.append(args[80])
                antargs.append(args[77])
                antargs.append(args[1])
                antargs.extend(args[87:107])
                self.ant = Antenna().init1(antargs)
                # scenesargs = args[3:5] + args[107] + args[1] + args[108]
                scenesargs = args[3:5]
                scenesargs.append(args[107])
                scenesargs.append(args[1])
                scenesargs.append(args[108])
                self.scenes = Cell2scenes().init1(scenesargs)
                return self

    def makeDataToOss(self):
        try:
            self.cell.makeDataToOss()
            self.rru.makeDataToOss()
            self.ant.makeDataToOss()
            self.scenes.makeDataToOss()
            return True
        except:
            return False

class Gsmcellindex(models.Model):
    cellname = models.CharField(max_length=512)
    lac = models.CharField(max_length=512)
    ci = models.CharField(max_length=512)
    nodebname = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    tchflow = models.FloatField(blank=True, null=True)
    resource_usage = models.FloatField(blank=True, null=True)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[1]
                lac1 = str(int(args[4]))
                ci1 = str(int(args[5]))
                self.lac = lac1
                self.ci = ci1
                self.nodebname = args[3]
                self.city = args[2] + u'市'
                self.tchflow = args[9]
                self.resource_usage = args[14]
        return self


class Wcdmacellindex(models.Model):
    cellname = models.CharField(max_length=512)
    lac = models.CharField(max_length=512)
    ci = models.CharField(max_length=512)
    nodebname = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    csflow = models.FloatField(blank=True, null=True)
    upflow = models.FloatField(blank=True, null=True)
    downflow = models.FloatField(blank=True, null=True)
    resource_usage = models.FloatField(blank=True, null=True)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[3]
                lac1 = str(int(args[6]))
                ci1 = str(int(args[5]))
                self.lac = lac1
                self.ci = ci1
                self.nodebname = args[2]
                self.city = args[1] + u'市'
                self.csflow = args[9]
                self.upflow = args[10]
                self.downflow = args[11]
                self.resource_usage = args[18]
        return self


class Ltecellindex(models.Model):
    cellname = models.CharField(max_length=512)
    lac = models.CharField(max_length=512)
    ci = models.CharField(max_length=512)
    nodebname = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    upflow = models.FloatField(blank=True, null=True)
    downflow = models.FloatField(blank=True, null=True)
    resource_usage = models.FloatField(blank=True, null=True)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[4]
                lac1 = str(args[3]).strip()
                ci1 = str(args[3]).strip()
                self.lac = lac1
                self.ci = ci1
                self.nodebname = args[3]
                self.city = args[1]
                self.upflow = args[5]
                self.downflow = args[6]
                self.resource_usage = args[7]
        return self
