#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
weekday = {'1':['20140901','20141201','20150105'],
           '2':[],
           '3':['20141008'],
           '4':[],
           '5':['20140801'],
           '6':['20141101'],
           '0':[]}
holiday = ['20140906','20140907','20140908','20141001','20141002',
           '20141003','20141004','20141005','20141006','20141007',
           '20150101','20150102','20150103',]
extra_workday = ['20140928','20141011','20150104']
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_in = open(os.path.join(data_path, 'weather_feature_mat.txt'))
data_array = list()
arrayOfLines = file_in.readlines()
for i in range(len(arrayOfLines)):
    arrayOfLines[i] = arrayOfLines[i].strip()
    arrayOfLines[i] = arrayOfLines[i].split(',')
    data_array.append(arrayOfLines[i][0])
first_day_per_month = weekday.values()
for i in first_day_per_month:
    if type(i) == list :
        for j in i :
            first_day_per_month.append(j)
indexs = []
for i in range(len(first_day_per_month)):
    if type(first_day_per_month[i]) == list :
        indexs.append(i)
indexs.sort(reverse= True)
for i in indexs:
    del first_day_per_month[i]

for i in data_array:
    if i in first_day_per_month or i in holiday or i in extra_workday:
            continue
    else:
        m = int(i)
        n = 1
        flag = True
        while flag:
            for day_type, days in weekday.iteritems():
                if str(m-n) in days :
                    d = int(day_type)
                    weekday[str((d + n) % 7)].append(i)
                    flag = False
            n += 1
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_out = open(os.path.join(data_path, 'weekday.txt'), 'w')
for day_type, days in weekday.iteritems():
    file_out.write(''.join([day_type, ':']))
    file_out.write('\n')
    for day in days:
        file_out.write(day)
        file_out.write('\n')
workday = []
restday = []
for day_type, days in weekday.iteritems():
    m = int(day_type)
    if m == 6 or m == 0 :
        for i in days :
            restday.append(i)
    else :
        for i in days :
            workday.append(i)
for i in extra_workday:
    workday.append(i)
workday.sort()
restday.sort()
holiday.sort()
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
fout1 = open(os.path.join(data_path, 'workday.txt'), 'w')
fout2 = open(os.path.join(data_path, 'restday.txt'), 'w')
fout3 = open(os.path.join(data_path, 'holiday.txt'), 'w')
for day in workday:
    fout1.write(day)
    fout1.write('\n')
for day in restday:
    fout2.write(day)
    fout2.write('\n')
for day in holiday:
    fout3.write(day)
    fout3.write('\n')
file_in.close()
file_out.close()
fout1.close()
fout2.close()
fout3.close()
