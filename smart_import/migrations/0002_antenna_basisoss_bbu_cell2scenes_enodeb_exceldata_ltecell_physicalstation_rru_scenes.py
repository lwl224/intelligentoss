# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-17 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_import', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasisOss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bbu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbuid', models.CharField(max_length=512)),
                ('bbuname', models.CharField(max_length=512)),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('district', models.CharField(max_length=512)),
                ('factory', models.CharField(max_length=512)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('enodebid3', models.CharField(max_length=512)),
                ('physicalstationid', models.CharField(max_length=512)),
                ('unittype', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Enodeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physicalstationnumb23g', models.CharField(max_length=512)),
                ('sourcetypes', models.CharField(max_length=512)),
                ('commonmode', models.CharField(max_length=512)),
                ('unittype', models.CharField(max_length=512)),
                ('hwversion', models.CharField(max_length=512)),
                ('swversion', models.CharField(max_length=512)),
                ('swbugversion', models.CharField(max_length=512)),
                ('s1ubandwidth', models.CharField(max_length=512)),
                ('enodebbandwidth1', models.CharField(max_length=512)),
                ('enodebbandwidth2', models.CharField(max_length=512)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('Carrier', models.CharField(max_length=512)),
                ('Sectortype', models.CharField(max_length=512)),
                ('bbunumb', models.CharField(max_length=512)),
                ('rrunumb', models.CharField(max_length=512)),
                ('rrunumb24G', models.CharField(max_length=512)),
                ('repeater', models.CharField(max_length=512)),
                ('bstype', models.CharField(max_length=512)),
                ('location', models.CharField(max_length=512)),
                ('bslevel', models.CharField(max_length=512)),
                ('mcc', models.CharField(max_length=512)),
                ('mnc', models.CharField(max_length=512)),
                ('enodebcell', models.CharField(max_length=512)),
                ('enodebip', models.CharField(max_length=512)),
                ('towerdelivery', models.CharField(max_length=512)),
                ('towerlocation', models.CharField(max_length=512)),
                ('towerlevel', models.CharField(max_length=512)),
                ('sharetelecom', models.CharField(max_length=512)),
                ('builder', models.CharField(max_length=512)),
                ('share', models.CharField(max_length=512)),
                ('sharebs', models.CharField(max_length=512)),
                ('customize1', models.CharField(max_length=512)),
                ('customize2', models.CharField(max_length=512)),
                ('customize3', models.CharField(max_length=512)),
                ('customize4', models.CharField(max_length=512)),
                ('customize5', models.CharField(max_length=512)),
                ('customize6', models.CharField(max_length=512)),
                ('customize7', models.CharField(max_length=512)),
                ('customize8', models.CharField(max_length=512)),
                ('customize9', models.CharField(max_length=512)),
                ('customize10', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='exceldata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('headImg', models.FileField(upload_to='./upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Physicalstation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physicalstationid', models.CharField(max_length=512)),
                ('physicalstationname', models.CharField(max_length=512)),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('district', models.CharField(max_length=512)),
                ('fulladdress', models.CharField(max_length=512)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('altitude', models.CharField(max_length=512)),
                ('isboundary', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Scenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('district', models.CharField(max_length=512)),
                ('scenesid', models.CharField(max_length=512)),
                ('scenesname', models.CharField(max_length=512)),
                ('parentscenes', models.CharField(max_length=512)),
                ('scenesdescription', models.CharField(max_length=3000)),
                ('scenesrange', models.CharField(max_length=3000)),
                ('sceneslon', models.FloatField(blank=True, null=True)),
                ('sceneslat', models.FloatField(blank=True, null=True)),
                ('firstscenes', models.CharField(max_length=512)),
                ('secondscenes', models.CharField(max_length=512)),
                ('hotregion', models.CharField(max_length=512)),
                ('vitalarea', models.CharField(max_length=512)),
                ('population', models.FloatField(blank=True, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('cell2g', models.CharField(max_length=512)),
                ('cell3g', models.CharField(max_length=512)),
                ('cell4g', models.CharField(max_length=512)),
                ('carrier2g', models.CharField(max_length=512)),
                ('carrier3g', models.CharField(max_length=512)),
                ('carrier4g', models.CharField(max_length=512)),
                ('fpoint2g', models.CharField(max_length=512)),
                ('fpoint3g', models.CharField(max_length=512)),
                ('fpoint4g', models.CharField(max_length=512)),
                ('mobilecover2g', models.CharField(max_length=512)),
                ('mobilecover3g', models.CharField(max_length=512)),
                ('mobilecover4g', models.CharField(max_length=512)),
                ('mobilefpoint', models.CharField(max_length=512)),
                ('telecomcover2g', models.CharField(max_length=512)),
                ('telecomcover3g', models.CharField(max_length=512)),
                ('telecomcover4g', models.CharField(max_length=512)),
                ('telecomfpoint', models.CharField(max_length=512)),
                ('sceneslevel', models.CharField(max_length=512)),
                ('customize1', models.CharField(max_length=512)),
                ('customize2', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('basisoss_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='smart_import.BasisOss')),
                ('antennaid', models.CharField(max_length=512)),
                ('antennaid1', models.CharField(max_length=512)),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('district', models.CharField(max_length=512)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('physicalstationid', models.CharField(max_length=512)),
                ('rruid', models.CharField(max_length=512)),
                ('cellid1', models.CharField(max_length=512)),
                ('directionangle', models.FloatField(blank=True, null=True)),
                ('antennaheight', models.FloatField(blank=True, null=True)),
                ('electricaldowntilt', models.CharField(max_length=512)),
                ('mechanicaltilt', models.CharField(max_length=512)),
                ('antennatypes', models.CharField(max_length=512)),
                ('beautifytypes', models.CharField(max_length=512)),
                ('antennafactory', models.CharField(max_length=512)),
                ('antennamodel', models.CharField(max_length=512)),
                ('antennanum', models.CharField(max_length=512)),
                ('horizontalpowerangle', models.CharField(max_length=512)),
                ('verticalpowerangle', models.CharField(max_length=512)),
                ('antennagain', models.CharField(max_length=512)),
                ('picture1', models.CharField(max_length=512)),
                ('picture2', models.CharField(max_length=512)),
                ('picture3', models.CharField(max_length=512)),
                ('picture4', models.CharField(max_length=512)),
                ('towermast', models.CharField(max_length=512)),
                ('txrxmod', models.CharField(max_length=512)),
                ('verticalrange', models.CharField(max_length=512)),
                ('install', models.CharField(max_length=512)),
            ],
            bases=('smart_import.basisoss',),
        ),
        migrations.CreateModel(
            name='Cell2scenes',
            fields=[
                ('basisoss_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='smart_import.BasisOss')),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('scenesid', models.CharField(max_length=512)),
                ('cellid1', models.CharField(max_length=512)),
                ('networktype', models.CharField(max_length=512)),
            ],
            bases=('smart_import.basisoss',),
        ),
        migrations.CreateModel(
            name='Ltecell',
            fields=[
                ('basisoss_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='smart_import.BasisOss')),
                ('cellname', models.CharField(max_length=256)),
                ('cellid1', models.CharField(max_length=256)),
                ('cellomcname', models.CharField(max_length=256)),
                ('province', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('district', models.CharField(max_length=256)),
                ('villages', models.CharField(max_length=256)),
                ('enodebid', models.CharField(max_length=256)),
                ('cellid2', models.CharField(max_length=256)),
                ('sector', models.CharField(max_length=256)),
                ('eutranCellid', models.CharField(max_length=256)),
                ('factory', models.CharField(max_length=256)),
                ('villagestypes', models.CharField(max_length=256)),
                ('MR', models.CharField(max_length=256)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('antennaid', models.CharField(max_length=256)),
                ('antennanum', models.CharField(max_length=256)),
                ('worktypes', models.CharField(max_length=256)),
                ('cp', models.CharField(max_length=256)),
                ('subframe', models.CharField(max_length=256)),
                ('specificsubframe', models.CharField(max_length=256)),
                ('remoterru', models.CharField(max_length=256)),
                ('upfpoint', models.CharField(max_length=256)),
                ('downfpoint', models.CharField(max_length=256)),
                ('pci', models.CharField(max_length=256)),
                ('pcilist', models.CharField(max_length=256)),
                ('cellmaxpower', models.CharField(max_length=256)),
                ('rspower', models.CharField(max_length=256)),
                ('atypepower1', models.CharField(max_length=256)),
                ('btypepower1', models.CharField(max_length=256)),
                ('atypepower2', models.CharField(max_length=256)),
                ('btypepower2', models.CharField(max_length=256)),
                ('bcchpower', models.CharField(max_length=256)),
                ('maxpower', models.CharField(max_length=256)),
                ('tac', models.CharField(max_length=256)),
                ('taclist', models.CharField(max_length=256)),
                ('operation', models.CharField(max_length=256)),
                ('updatatime', models.CharField(max_length=256)),
                ('coveragetypes', models.CharField(max_length=256)),
                ('coveragerange', models.CharField(max_length=256)),
                ('plmn', models.CharField(max_length=256)),
                ('mbms', models.CharField(max_length=256)),
                ('band', models.CharField(max_length=256)),
                ('centerfrequency', models.CharField(max_length=256)),
                ('bandwidth', models.CharField(max_length=256)),
                ('downCyclicPrefix', models.CharField(max_length=256)),
                ('upCyclicPrefix', models.CharField(max_length=256)),
                ('upbandwidth', models.CharField(max_length=256)),
                ('downbandwidth', models.CharField(max_length=256)),
                ('astat', models.CharField(max_length=256)),
                ('hs', models.CharField(max_length=256)),
                ('txrxmod', models.CharField(max_length=256)),
                ('worktypes1', models.CharField(max_length=256)),
                ('leadingformat', models.CharField(max_length=256)),
                ('isblocking', models.CharField(max_length=256)),
                ('boundarycell', models.CharField(max_length=256)),
                ('boundaryname', models.CharField(max_length=256)),
                ('csbf', models.CharField(max_length=256)),
                ('hs2', models.CharField(max_length=256)),
                ('istelecom', models.CharField(max_length=256)),
                ('build', models.CharField(max_length=256)),
                ('sharingmode', models.CharField(max_length=256)),
                ('isca', models.CharField(max_length=256)),
                ('catypes', models.CharField(max_length=256)),
                ('catypeassociation', models.CharField(max_length=256)),
                ('camaincellid', models.CharField(max_length=256)),
                ('customize1', models.CharField(max_length=256)),
                ('customize2', models.CharField(max_length=256)),
                ('customize3', models.CharField(max_length=256)),
                ('customize4', models.CharField(max_length=256)),
                ('customize5', models.CharField(max_length=256)),
                ('customize6', models.CharField(max_length=256)),
                ('customize7', models.CharField(max_length=256)),
                ('customize8', models.CharField(max_length=256)),
                ('customize9', models.CharField(max_length=256)),
                ('customize10', models.CharField(max_length=256)),
            ],
            bases=('smart_import.basisoss',),
        ),
        migrations.CreateModel(
            name='Rru',
            fields=[
                ('basisoss_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='smart_import.BasisOss')),
                ('rruid', models.CharField(max_length=512)),
                ('rruname', models.CharField(max_length=512)),
                ('province', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('district', models.CharField(max_length=512)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('bbuid', models.CharField(max_length=512)),
                ('cellid1', models.CharField(max_length=512)),
                ('physicalstationid', models.CharField(max_length=512)),
                ('rrutypes', models.CharField(max_length=512)),
                ('rruport', models.CharField(max_length=512)),
                ('txrxtypes', models.CharField(max_length=512)),
            ],
            bases=('smart_import.basisoss',),
        ),
    ]
