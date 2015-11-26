#!/usr/bin/python
# -*- coding: utf-8 -*-
#calculate pupulation each line, every day and every hour(6-21), and split those data into two files
import os
from operator import itemgetter
###############################################################################
#import as dict
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'original_data2')
file_in = open(os.path.join(data_path, 'gd_train_data.txt'))
data_dict = {}
data_dict['线路6'] = {}
data_dict['线路11'] = {}
for each_line in file_in:
    S = each_line.strip()
    array_of_line = S.split(',')
    for key in data_dict.keys():
        if key in S:
            if array_of_line[5] in data_dict[key]:
                data_dict[key][array_of_line[5]] += 1
            else:
                data_dict[key][array_of_line[5]] = 1
file_in.close()
###############################################################################
#convert dict to list and sort by date
line_6_data = []
line_11_data = []
for date, value in data_dict['线路6'].iteritems():
    line_6_data.append([date, value])
for date, value in data_dict['线路11'].iteritems():
    line_11_data.append([date, value])
line_6_data = sorted(line_6_data, key=itemgetter(0))
line_11_data = sorted(line_11_data, key=itemgetter(0))
###############################################################################
#delete list elements with time earlier than 6 o'clock or later than 21 o'clock
indexs_6 = []
indexs_11 = []
for data in line_6_data:
    temp_int =  int(data[0][-2:])
    if temp_int<6 or temp_int>21:
        indexs_6.append(line_6_data.index(data))
for data in line_11_data:
    temp_int =  int(data[0][-2:])
    if temp_int<6 or temp_int>21:
        indexs_11.append(line_11_data.index(data))
indexs_6.sort(reverse=  True)
indexs_11.sort(reverse=  True)
for i in indexs_6:
    del line_6_data[i]
for i in indexs_11:
    del line_11_data[i]
###############################################################################
#delete list elements with number of population less than 300 in line 6 or less than 200 in line 11
#indexs_6 = []
#indexs_11 = []
#for data in line_6_data:
#    if data[1] < 300:
#        indexs_6.append(line_6_data.index(data))
#for data in line_11_data:
#    if data[1] < 200:
#        indexs_11.append(line_11_data.index(data))
#indexs_6.sort(reverse=  True)
#indexs_11.sort(reverse=  True)
#for i in indexs_6:
#    del line_6_data[i]
#for i in indexs_11:
#    del line_11_data[i]


###############################################################################
#Output to two new files
data_path = os.path.join(parent_path, 'train_data')
file_out1 = open(os.path.join(data_path, 'line6_stat.txt'), 'w')
file_out2 = open(os.path.join(data_path, 'line11_stat.txt'), 'w')
for i in line_6_data:
    file_out1.write(','.join([i[0], str(i[1])]))
    file_out1.write('\n')
for j in line_11_data:
    file_out2.write(','.join([j[0], str(j[1])]))
    file_out2.write('\n')
file_out1.close()
file_out2.close()