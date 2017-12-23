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

from smart_import.models import *
from tool.oss_data_treating import Databases_dataSave, ScrapyDataAcquisition
import cPickle as pickle
import random
import string


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
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
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
    Databases_dataSave().original_data_save()
    return HttpResponseRedirect(reverse('homepage'))


def download(request):
    ScrapyDataAcquisition().get_original_data()
    return HttpResponseRedirect(reverse('homepage'))


class ExcelForm(forms.Form):
    excelfile = forms.FileField()


def upexcel(request):
    user = request.user if request.user.is_authenticated() else None
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    if request.method == "POST":
        uf = ExcelForm(request.POST, request.FILES)
        if uf.is_valid():
            cell_list = pretreatment_uploading_excel(salt, uf)
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
            }

            return render_to_response('management/upexcel.html', content)
    else:
        uf = ExcelForm()
    return render_to_response('management/upexcel.html', {'uf': uf, 'user': user, })


def pretreatment_uploading_excel(salt, uf):
    # 获取表单信息
    excelfile = uf.cleaned_data['excelfile']
    wb = xlrd.open_workbook(filename=None, file_contents=excelfile.read())  # 关键点在于这里
    # 写入数据库
    table = wb.sheet_by_index(0)  # 获取工作表
    n = 1
    cell_list = []
    for line in range(n, table.nrows):  # nrows = table.nrows 行数
        row = table.row_values(line)  # ncols = table.ncols 列数
        if row:  # 查看行值是否为空
            test11 = Cellunion().init1(row)
            cell_list.append(test11)
    if not os.path.exists('./' + 'tool/data/temp/'):
        os.makedirs('./' + 'tool/data/temp/')
    with open('tool/data/temp/%s.pkl' % salt, 'wb') as f:
        pickle.dump(cell_list, f)
    return cell_list


def addcellunion(request, salt):
    user = request.user if request.user.is_authenticated() else None
    try:
        flag = True
        with open('tilt/data/temp/%s.pkl' % salt, 'rb') as f:
            cell_list = pickle.load(f)
            for cellunim in cell_list:
                flag = flag and cellunim.makeDataToOss()

    finally:
        os.remove('tilt/data/temp/%s.pkl' % salt)
    if flag:
        content = {
            'user': user,
            'flagstr': '导入成功',
        }

        return render_to_response('management/importresult.html', content)
    else:
        return HttpResponse(u'完成失败')


def big_file_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open('./tool/data/'+file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = u"cell模板.xlsx"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response


