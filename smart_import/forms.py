# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/12/25'
"""
import sys
from django import forms
from smart_import.models import *

reload(sys)
sys.setdefaultencoding('utf8')


# IntegerField
# FloatField

class ContactForm(forms.Form):
    cellname = forms.CharField()
    cellid1 = forms.CharField()
    cellomcname = forms.CharField()
    province = forms.CharField()
    city = forms.CharField()
    district = forms.CharField()
    villages = forms.CharField()
    enodebid = forms.CharField()
    cellid2 = forms.CharField()
    sector = forms.CharField()
    eutranCellid = forms.CharField()
    factory = forms.CharField()
    villagestypes = forms.CharField()
    mr = forms.CharField()
    lon = forms.FloatField()
    lat = forms.FloatField()
    antennaid = forms.CharField()
    antennanum = forms.IntegerField()
    worktypes = forms.CharField()
    cp = forms.CharField()
    subframe = forms.CharField()
    specificsubframe = forms.CharField()
    remoterru = forms.CharField()
    upfpoint = forms.FloatField()
    downfpoint = forms.FloatField()
    pci = forms.IntegerField(max_value=550)
    pcilist = forms.CharField()
    cellmaxpower = forms.FloatField()
    rspower = forms.CharField()
    atypepower1 = forms.CharField()
    btypepower1 = forms.CharField()
    atypepower2 = forms.CharField()
    btypepower2 = forms.CharField()
    bcchpower = forms.FloatField()
    maxpower = forms.FloatField()
    tac = forms.IntegerField()
    taclist = forms.CharField(required=False)
    operation = forms.CharField()
    updatatime = forms.CharField()
    coveragetypes = forms.CharField()
    coveragerange = forms.CharField()
    plmn = forms.CharField()
    mbms = forms.CharField(required=False)
    band = forms.IntegerField()
    centerfrequency = forms.CharField()
    bandwidth = forms.CharField()
    downCyclicPrefix = forms.CharField()
    upCyclicPrefix = forms.CharField()
    upbandwidth = forms.CharField()
    downbandwidth = forms.CharField()
    astat = forms.CharField()
    hs = forms.CharField(required=False)
    txrxmod = forms.CharField()
    worktypes1 = forms.CharField()
    leadingformat = forms.CharField(required=False)
    isblocking = forms.CharField(required=False)
    boundarycell = forms.CharField(required=False)
    boundaryname = forms.CharField(required=False)
    csbf = forms.CharField()
    hs2 = forms.CharField(required=False)
    istelecom = forms.CharField()
    build = forms.CharField()
    sharingmode = forms.CharField()
    isca = forms.CharField()
    catypes = forms.CharField()
    catypeassociation = forms.CharField()
    camaincellid = forms.CharField()
    customize1 = forms.CharField()
    customize2 = forms.CharField()
    customize3 = forms.CharField()
    customize4 = forms.CharField()
    customize5 = forms.CharField()
    customize6 = forms.CharField()
    customize7 = forms.CharField()
    customize8 = forms.CharField()
    customize9 = forms.CharField(required=False)
    customize10 = forms.CharField(required=False)
    rruid = forms.CharField()
    rruname = forms.CharField()
    bbuid = forms.CharField()
    physicalstationid = forms.CharField()
    rrutypes = forms.CharField()
    rruport = forms.CharField()
    txrxtypes = forms.CharField()
    antennaid_1 = forms.CharField()
    antennaid1 = forms.CharField()
    rruid_1 = forms.CharField(required=False)
    directionangle = forms.FloatField()
    antennaheight = forms.FloatField()
    electricaldowntilt = forms.CharField()
    mechanicaltilt = forms.CharField()
    antennatypes = forms.CharField()
    beautifytypes = forms.CharField()
    antennafactory = forms.CharField()
    antennamodel = forms.CharField()
    antennanum_1 = forms.CharField()
    horizontalpowerangle = forms.CharField()
    verticalpowerangle = forms.CharField()
    antennagain = forms.CharField()
    picture1 = forms.CharField()
    picture2 = forms.CharField()
    picture3 = forms.CharField()
    picture4 = forms.CharField()
    towermast = forms.CharField()
    txrxmod_1 = forms.CharField()
    verticalrange = forms.CharField()
    install = forms.CharField(required=False)
    scenesid = forms.CharField()
    networktype = forms.CharField()
    def make_clean(self, cleam_data):
        # cleam_data={'name':'coveragetypes','mapping':COVER_TYPElist,}
        cleam = self.cleaned_data[cleam_data['name']]
        if cleam not in cleam_data['mapping'].viewkeys():
            raise forms.ValidationError(u'不在有效数据范围之内')
        return cleam
    def clean_coveragetypes(self):
        cleam_data = {'name': 'coveragetypes', 'mapping': COVER_TYPElist, }
        return self.make_clean(cleam_data)

    def clean_city(self):
        cleam_data = {'name': 'city', 'mapping': CITYID, }
        return self.make_clean(cleam_data)

    def clean_villagestypes(self):
        cleam_data = {'name': 'villagestypes', 'mapping': ADMIN_REGIONSlist, }
        return self.make_clean(cleam_data)

    def clean_district(self):
        cleam_data = {'name': 'district', 'mapping': DISTRICT_ID, }
        return self.make_clean(cleam_data)

    def clean_mr(self):
        cleam_data = {'name': 'mr', 'mapping': IS_Mrlist, }
        return self.make_clean(cleam_data)

    def clean_worktypes(self):
        cleam_data = {'name': 'worktypes', 'mapping': DUP_MODElist, }
        return self.make_clean(cleam_data)

    def clean_remoterru(self):
        cleam_data = {'name': 'remoterru', 'mapping': RRUCELL_FLAGlist, }
        return self.make_clean(cleam_data)

    def clean_astat(self):
        cleam_data = {'name': 'astat', 'mapping': CELL_ACTIVE_STATElist, }
        return self.make_clean(cleam_data)

    def clean_hs(self):
        cleam_data = {'name': 'hs', 'mapping': HIGH_SPEED_FLAGlist, }
        return self.make_clean(cleam_data)

    def clean_txrxmod(self):
        cleam_data = {'name': 'txrxmod', 'mapping': TX_RX_MODElist, }
        return self.make_clean(cleam_data)

    def clean_csbf(self):
        cleam_data = {'name': 'csbf', 'mapping': CSFBlist, }
        return self.make_clean(cleam_data)

    def clean_build(self):
        cleam_data = {'name': 'build', 'mapping': COMPANYlist, }
        return self.make_clean(cleam_data)

    def clean_sharingmode(self):
        cleam_data = {'name': 'sharingmode', 'mapping': SHARED_TYPElsit, }
        return self.make_clean(cleam_data)

    def clean_factory(self):
        cleam_data = {'name': 'factory', 'mapping': VENDOR_Idlsit, }
        return self.make_clean(cleam_data)

    def clean_rrutypes(self):
        cleam_data = {'name': 'rrutypes', 'mapping': RRU_MODELlist, }
        return self.make_clean(cleam_data)