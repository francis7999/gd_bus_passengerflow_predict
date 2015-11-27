#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
cur_path = os.getcwd()
data_path = os.path.join(cur_path, 'history_submitted_files/11.27')
file_in1 = open(os.path.join(data_path, 'GBDT_predict_data.txt'))
file_in2 = open(os.path.join(data_path, 'DT_predict_data.txt'))
arrayOfLines1 = file_in1.readlines()
listFromLines1= []
GBDT_line6_x = {}
GBDT_line6_x['20150101'] = []
GBDT_line6_x['20150102'] = []
GBDT_line6_x['20150103'] = []
GBDT_line6_x['20150104'] = []
GBDT_line6_x['20150105'] = []
GBDT_line6_x['20150106'] = []
GBDT_line6_x['20150107'] = []
GBDT_line6_y = {}
GBDT_line6_y['20150101'] = []
GBDT_line6_y['20150102'] = []
GBDT_line6_y['20150103'] = []
GBDT_line6_y['20150104'] = []
GBDT_line6_y['20150105'] = []
GBDT_line6_y['20150106'] = []
GBDT_line6_y['20150107'] = []
for line in arrayOfLines1:
    line = line.strip()
    listFromLines1.append(line.split(','))
for line in listFromLines1:
    if cmp(line[0], '线路6') == 0 :
        GBDT_line6_x[line[1]].append(line[2])
        GBDT_line6_y[line[1]].append(line[3])
arrayOfLines2 = file_in2.readlines()
listFromLines2= []
DT_line6_x = {}
DT_line6_x['20150101'] = []
DT_line6_x['20150102'] = []
DT_line6_x['20150103'] = []
DT_line6_x['20150104'] = []
DT_line6_x['20150105'] = []
DT_line6_x['20150106'] = []
DT_line6_x['20150107'] = []
DT_line6_y = {}
DT_line6_y['20150101'] = []
DT_line6_y['20150102'] = []
DT_line6_y['20150103'] = []
DT_line6_y['20150104'] = []
DT_line6_y['20150105'] = []
DT_line6_y['20150106'] = []
DT_line6_y['20150107'] = []
for line in arrayOfLines2:
    line = line.strip()
    listFromLines2.append(line.split(','))
for line in listFromLines2:
    if cmp(line[0], '线路6') == 0 :
        DT_line6_x[line[1]].append(line[2])
        DT_line6_y[line[1]].append(line[3])


plt.figure(figsize = (15, 6))
plt.plot(GBDT_line6_x['20150101'], GBDT_line6_y['20150101'], 'o',
         DT_line6_x['20150101'], DT_line6_y['20150101'], 'or' )
plt.show()