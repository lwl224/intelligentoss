# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.test import TestCase

# Create your tests here.

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


def clean_city(self):
    city_name = self.cleaned_data['city']
    if city_name not in CITYID.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return city_name


def clean_villagestypes(self):
    villagestypes = self.cleaned_data['villagestypes']
    if villagestypes not in ADMIN_REGIONSlist.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return villagestypes


def clean_district(self):
    district = self.cleaned_data['district']
    if district not in DISTRICT_ID.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return district


def clean_mr(self):
    mr = self.cleaned_data['mr']
    if mr not in IS_Mrlist.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return mr


def clean_worktypes(self):
    worktypes = self.cleaned_data['worktypes']
    if worktypes not in DUP_MODElist.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return worktypes


def clean_remoterru(self):
    remoterru = self.cleaned_data['remoterru']
    if remoterru not in RRUCELL_FLAGlist.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return remoterru

def clean_coveragetypes(self):
    coveragetypes = self.cleaned_data['coveragetypes']
    if coveragetypes not in COVER_TYPElist.viewkeys():
        raise forms.ValidationError("You have input error!")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return coveragetypes

def make_clean(self,cleam_data):
    # cleam_data={'name':'coveragetypes','mapping':COVER_TYPElist,}
    cleam = self.cleaned_data[cleam_data['name']]
    if cleam not in cleam_data['mapping'].viewkeys():
        raise forms.ValidationError("You have input error!")
    return cleam


print "南宁市" in CITYID.viewkeys()
print "城区" in ADMIN_REGIONSlist.viewkeys()
print "已采集" in IS_Mrlist.viewkeys()
print "FDD" in DUP_MODElist.viewkeys()
# print "南宁市" not in CITYID
