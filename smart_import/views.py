# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xlrd
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.http import StreamingHttpResponse
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from smart_import.forms import ContactForm
from smart_import.models import *
from tool.oss_data_treating import Databases_dataSave, ScrapyDataAcquisition
import cPickle as pickle
import random
import string
from gevent import monkey
import gevent

monkey.patch_socket()


# Create your views here.



def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/index.html', content)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/login.html', content)


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''),
                                     region=request.POST.get('region', ''),
                                     department=request.POST.get('department', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/signup.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/set_password.html', content)


def view_cell(request):
    user = request.user if request.user.is_authenticated() else None
    # category_list = Book.objects.values_list('category', flat=True).distinct()
    cell_list = Ltecell.objects.all()

    query_category = 'all'
    paginator = Paginator(cell_list, 25)
    page = request.GET.get('page')
    try:
        cell_list = paginator.page(page)
    except PageNotAnInteger:
        cell_list = paginator.page(1)
    except EmptyPage:
        cell_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_book',
        # 'category_list': category_list,
        'query_category': query_category,
        'cell_list': cell_list,
    }
    return render(request, 'management/view_cell_list.html', content)


def initialization(request):
    user = request.user if request.user.is_authenticated() else None
    try:
        Databases_dataSave().original_data_save()
        return HttpResponseRedirect(reverse('homepage'))
    except:
        # flagstr = '导入数据失败'
        content = {
            'user': user,
            'active_menu': 'view_book',
            # 'category_list': category_list,
            'flagstr': '导入数据失败',
        }
        return render(request, 'management/importresult.html', content)


def download(request):
    user = request.user if request.user.is_authenticated() else None
    try:
        ScrapyDataAcquisition().get_original_data()
        return HttpResponseRedirect(reverse('homepage'))
    except:
        # flagstr = '导入数据失败'
        content = {
            'user': user,
            'active_menu': 'view_book',
            # 'category_list': category_list,
            'flagstr': '爬取数据失败',
        }
        return render(request, 'management/importresult.html', content)


class ExcelForm(forms.Form):
    excelfile = forms.FileField()


def upexcel(request):
    user = request.user if request.user.is_authenticated() else None
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    if request.method == "POST":
        excelfile = ExcelForm(request.POST, request.FILES, auto_id=False)
        if excelfile.is_valid():
            cell_list = pretreatment_uploading_excel(salt, excelfile)
            check_flag = check_all_cellunion(cell_list)
            query_category = 'all'
            paginator = Paginator(cell_list, 10)
            page = request.GET.get('page')
            try:
                cell_list = paginator.page(page)
            except PageNotAnInteger:
                cell_list = paginator.page(1)
            except EmptyPage:
                cell_list = paginator.page(paginator.num_pages)
            content = {
                'user': user,
                'active_menu': 'view_book',
                'query_category': query_category,
                'cell_list': cell_list,
                'filtname': salt,
                'check_flag': check_flag
            }

            return render_to_response('management/upexcel.html', content)
    else:
        excelfile = ExcelForm(auto_id=False)
    return render_to_response('management/upexcel.html', {'excelfile': excelfile, 'user': user, })


def pretreatment_uploading_excel(salt, uf):
    # 获取表单信息
    excelfile = uf.cleaned_data['excelfile']
    open_excelfile = xlrd.open_workbook(filename=None, file_contents=excelfile.read())
    cell_table = open_excelfile.sheet_by_index(0)  # 获取工作表
    star_num = 1
    cellunion_list = []
    check_cellunion_data(cell_table, cellunion_list, star_num)
    save_cellunion(cellunion_list, salt)
    return cellunion_list


def save_cellunion(cellunion_list, salt):
    if not os.path.exists('./' + 'tool/data/temp/'):
        os.makedirs('./' + 'tool/data/temp/')
    with open('tool/data/temp/%s.pkl' % salt, 'wb') as f:
        pickle.dump(cellunion_list, f)


def check_all_cellunion(cellunion_list):
    check_flag = True
    for cellunion in cellunion_list:
        if cellunion.check_is == '通过':
            check_flag = check_flag & True
        else:
            check_flag = check_flag & False
    return check_flag


def check_cellunion_data(cell_table, cellunion_list, star_num):
    def excel_initial_contactForm(*args):
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                union_from_lte = ContactForm({'cellname': args[0],
                                              'cellid1': args[1],
                                              'cellomcname': args[2],
                                              'province': args[3],
                                              'city': args[4],
                                              'district': args[5],
                                              'villages': args[6],
                                              'enodebid': args[7],
                                              'cellid2': args[8],
                                              'sector': args[9],
                                              'eutranCellid': args[10],
                                              'factory': args[11],
                                              'villagestypes': args[12],
                                              'mr': args[13],
                                              'lon': args[14],
                                              'lat': args[15],
                                              'antennaid': args[16],
                                              'antennanum': args[17],
                                              'worktypes': args[18],
                                              'cp': args[19],
                                              'subframe': args[20],
                                              'specificsubframe': args[21],
                                              'remoterru': args[22],
                                              'upfpoint': args[23],
                                              'downfpoint': args[24],
                                              'pci': args[25],
                                              'pcilist': args[26],
                                              'cellmaxpower': args[27],
                                              'rspower': args[28],
                                              'atypepower1': args[29],
                                              'btypepower1': args[30],
                                              'atypepower2': args[31],
                                              'btypepower2': args[32],
                                              'bcchpower': args[33],
                                              'maxpower': args[34],
                                              'tac': args[35],
                                              'taclist': args[36],
                                              'operation': args[37],
                                              'updatatime': args[38],
                                              'coveragetypes': args[39],
                                              'coveragerange': args[40],
                                              'plmn': args[41],
                                              'mbms': args[42],
                                              'band': args[43],
                                              'centerfrequency': args[44],
                                              'bandwidth': args[45],
                                              'downCyclicPrefix': args[46],
                                              'upCyclicPrefix': args[47],
                                              'upbandwidth': args[48],
                                              'downbandwidth': args[49],
                                              'astat': args[50],
                                              'hs': args[51],
                                              'txrxmod': args[52],
                                              'worktypes1': args[53],
                                              'leadingformat': args[54],
                                              'isblocking': args[55],
                                              'boundarycell': args[56],
                                              'boundaryname': args[57],
                                              'csbf': args[58],
                                              'hs2': args[59],
                                              'istelecom': args[60],
                                              'build': args[61],
                                              'sharingmode': args[62],
                                              'isca': args[63],
                                              'catypes': args[64],
                                              'catypeassociation': args[65],
                                              'camaincellid': args[66],
                                              'customize1': args[67],
                                              'customize2': args[68],
                                              'customize3': args[69],
                                              'customize4': args[70],
                                              'customize5': args[71],
                                              'customize6': args[72],
                                              'customize7': args[73],
                                              'customize8': args[74],
                                              'customize9': args[75],
                                              'customize10': args[76],
                                              'rruid': args[77],
                                              'rruname': args[78],
                                              'bbuid': args[79],
                                              'physicalstationid': args[80],
                                              'rrutypes': args[81],
                                              'rruport': args[82],
                                              'txrxtypes': args[83],
                                              'antennaid_1': args[84],
                                              'antennaid1': args[85],
                                              'rruid_1': args[86],
                                              'directionangle': args[87],
                                              'antennaheight': args[88],
                                              'electricaldowntilt': args[89],
                                              'mechanicaltilt': args[90],
                                              'antennatypes': args[91],
                                              'beautifytypes': args[92],
                                              'antennafactory': args[93],
                                              'antennamodel': args[94],
                                              'antennanum_1': args[95],
                                              'horizontalpowerangle': args[96],
                                              'verticalpowerangle': args[97],
                                              'antennagain': args[98],
                                              'picture1': args[99],
                                              'picture2': args[100],
                                              'picture3': args[101],
                                              'picture4': args[102],
                                              'towermast': args[103],
                                              'txrxmod_1': args[104],
                                              'verticalrange': args[105],
                                              'install': args[106],
                                              'scenesid': args[107],
                                              'networktype': args[108],

                                              })
        return union_from_lte

    for line in range(star_num, cell_table.nrows):  # nrows = table.nrows 行数
        row = cell_table.row_values(line)  # ncols = table.ncols 列数
        unifrom = excel_initial_contactForm(row)
        if unifrom.is_valid():  # 查看行值是否符合规范
            cellunion_example = Cellunion().init1(row)
            cellunion_example.check_is = '通过'
            cellunion_list.append(cellunion_example)

        else:
            cellunion_example = Cellunion().init1(row)
            cellunion_example.check_is = error_message(unifrom)
            cellunion_list.append(cellunion_example)


def error_message(unifrom):
    formname_map = {u'cellname': u'小区别名',
                    u'cellid1': u'小区标识',
                    u'cellomcname': u'小区网管名称',
                    u'province': u'省份',
                    u'city': u'所属城市',
                    u'district': u'所属区县',
                    u'villages': u'乡镇',
                    u'enodebid': u'所属eNodeB标识',
                    u'cellid2': u'小区标识码',
                    u'sector': u'所属扇区编号',
                    u'eutranCellid': u'设备厂家EutranCell标识',
                    u'factory': u'设备厂家',
                    u'villagestypes': u'所属行政区域类型',
                    u'mr': u'是否采集MR',
                    u'lon': u'经度',
                    u'lat': u'纬度',
                    u'antennaid': u'相关联的天线列表',
                    u'antennanum': u'天线数',
                    u'worktypes': u'双工方式',
                    u'cp': u'采用的cp类型',
                    u'subframe': u'子帧配置类型',
                    u'specificsubframe': u'特殊子帧配置类型',
                    u'remoterru': u'是否为RRU小区',
                    u'upfpoint': u'上行频点',
                    u'downfpoint': u'下行频点',
                    u'pci': u'物理小区识别码',
                    u'pcilist': u'物理小区识别码列表',
                    u'cellmaxpower': u'小区配置的载频发射功率',
                    u'rspower': u'参考信号（RS）的每RE平均发射功率',
                    u'atypepower1': u'A类符号上每RE平均功率与RS占用的RE平均功率的比值',
                    u'btypepower1': u'B类符号上每RE平均功率与RS占用的RE平均功率的比值',
                    u'atypepower2': u'A类符号功率比值',
                    u'btypepower2': u'B类符号功率比值',
                    u'bcchpower': u'广播信道功率',
                    u'maxpower': u'最大传输功率',
                    u'tac': u'跟踪区编码',
                    u'taclist': u'跟踪区列表',
                    u'operation': u'运行状态',
                    u'updatatime': u'状态变更时间',
                    u'coveragetypes': u'小区覆盖类型',
                    u'coveragerange': u'小区覆盖范围',
                    u'plmn': u'PLMN标识的列表',
                    u'mbms': u'小区MBMS开关',
                    u'band': u'频段指示',
                    u'centerfrequency': u'中心载频的信道号',
                    u'bandwidth': u'带宽',
                    u'downCyclicPrefix': u'下行循环前缀长度',
                    u'upCyclicPrefix': u'上行循环前缀长度',
                    u'upbandwidth': u'上行带宽',
                    u'downbandwidth': u'下行带宽',
                    u'astat': u'小区激活状态',
                    u'hs': u'高速小区指示',
                    u'txrxmod': u'发送和接收模式',
                    u'worktypes1': u'工作模式',
                    u'leadingformat': u'前导格式',
                    u'isblocking': u'小区是否闭塞',
                    u'boundarycell': u'是否为省际边界小区',
                    u'boundaryname': u'省际边界小区相邻省份名称',
                    u'csbf': u'CSFB回落网络优先级',
                    u'hs2': u'是否高铁二层小区',
                    u'istelecom': u'是否电信共享小区',
                    u'build': u'建站单位',
                    u'sharingmode': u'共享方式',
                    u'isca': u'是否载波聚合小区',
                    u'catypes': u'载波聚合类型',
                    u'catypeassociation': u'载波聚合频段组合',
                    u'camaincellid': u'主载波小区CELL ID',
                    u'customize1': u'自定义字段1',
                    u'customize2': u'自定义字段2',
                    u'customize3': u'自定义字段3',
                    u'customize4': u'自定义字段4',
                    u'customize5': u'自定义字段5',
                    u'customize6': u'自定义字段6',
                    u'customize7': u'自定义字段7',
                    u'customize8': u'自定义字段8',
                    u'customize9': u'自定义字段9',
                    u'customize10': u'自定义字段10',
                    u'rruid': u'RRU采集前置标识',
                    u'rruname': u'RRU网管名称',
                    u'bbuid': u'所属bbu标识',
                    u'physicalstationid': u'所属物理站编号',
                    u'rrutypes': u'RRU类型',
                    u'rruport': u'RRU端口',
                    u'txrxtypes': u'发送和接收模式',
                    u'antennaid_1': u'天线编号',
                    u'antennaid1': u'天线在采集前置中的唯一标识',
                    u'rruid_1': u'所属RRU',
                    u'directionangle': u'天线方向角',
                    u'antennaheight': u'天线挂高',
                    u'electricaldowntilt': u'电子下倾角',
                    u'mechanicaltilt': u'机械倾角',
                    u'antennatypes': u'天线类型',
                    u'beautifytypes': u'美化类型',
                    u'antennafactory': u'天线厂家',
                    u'antennamodel': u'天线型号',
                    u'antennanum_1': u'天线端口数量',
                    u'horizontalpowerangle': u'水平半功率角',
                    u'verticalpowerangle': u'垂直半功率角',
                    u'antennagain': u'天线增益',
                    u'picture1': u'天线环境照片附件列表',
                    u'picture2': u'天线与覆盖目标照片附件列表',
                    u'picture3': u'地理化呈现照片附件',
                    u'picture4': u'存在问题照片附件列表',
                    u'towermast': u'塔桅类型',
                    u'txrxmod_1': u'发送和接收模式',
                    u'verticalrange': u'天线到铁轨的垂直距离',
                    u'install': u'天线安装物理基础类型',
                    u'scenesid': u'场景编号',
                    u'networktype': u'网络类型',
                    }
    error_message_str = '不通过:'
    for error in unifrom.errors:
        ss=unifrom.errors[error][0]

        error_message_str = error_message_str + formname_map[unicode(error, "utf-8")] + unifrom.errors[error][0]

    return error_message_str


def addcellunion(request, salt):
    user = request.user if request.user.is_authenticated() else None
    all_flag = ask_oss_cell_save(salt)
    if all_flag:
        content = {
            'user': user,
            'flagstr': '导入成功',
        }

        return render_to_response('management/importresult.html', content)
    else:
        return HttpResponse(u'完成失败')


def ask_oss_cell_save(salt):
    try:
        all_flag = True
        with open('tool/data/temp/%s.pkl' % salt, 'rb') as f:
            cell_list = pickle.load(f)
            for cellunim in cell_list:
                gevent_ask_cell_save = gevent.spawn(cellunim.cell.makeDataToOss)
                gevent_ask_cell_save.join()
                all_flag = all_flag & gevent_ask_cell_save.successful()
                gevent_ask_rru_save = gevent.spawn(cellunim.rru.makeDataToOss)
                gevent_ask_rru_save.join()
                all_flag = all_flag & gevent_ask_rru_save.successful()
                gevent_ask_ant_save = gevent.spawn(cellunim.ant.makeDataToOss)
                gevent_ask_ant_save.join()
                all_flag = all_flag & gevent_ask_ant_save.successful()
                gevent_ask_scenes_save = gevent.spawn(cellunim.scenes.makeDataToOss)
                gevent_ask_scenes_save.join()
                all_flag = all_flag & gevent_ask_scenes_save.successful()
    except:
        raise LookupError
    finally:
        os.remove('tool/data/temp/%s.pkl' % salt)
    return all_flag


def big_file_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open('./tool/data/' + file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = u"cell-模板.xls"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/vnd.ms-excel'
    file_name = r'ltecell.xls'
    response['Content-Disposition'] = 'attachment;filename=' + file_name
    return response
