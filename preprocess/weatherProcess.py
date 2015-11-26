#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'original_data2')
fr = open(os.path.join(data_path, 'gd_weather_report.txt'))
arrayOfLines = fr.readlines()
numberOfLines = len(arrayOfLines)
for i in range(numberOfLines):
		arrayOfLines[i] = arrayOfLines[i].strip()
for i in range(0,9):
		l = list(arrayOfLines[i])
		l[4] = '0'
		l[6] = '0'
		arrayOfLines[i] = ''.join(l)
for i in range(9,31):
		l = list(arrayOfLines[i])
		l[4] = '0'
		l.pop(6)
		arrayOfLines[i] = ''.join(l)
for i in range(31,40):
		l = list(arrayOfLines[i])
		l[4] = '0'
		l[6] = '0'
		arrayOfLines[i] = ''.join(l)
for i in range(40,61):
		l = list(arrayOfLines[i])
		l[4] = '0'
		l.pop(6)
		arrayOfLines[i] = ''.join(l)
for i in range(61,70):
		l = list(arrayOfLines[i])
		l[7] = '0'
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(70,92):
		l = list(arrayOfLines[i])
		l.pop(7)
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(92,101):
		l = list(arrayOfLines[i])
		l[7] = '0'
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(101,122):
		l = list(arrayOfLines[i])
		l.pop(7)
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(122,131):
		l = list(arrayOfLines[i])
		l[7] = '0'
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(131,153):
		l = list(arrayOfLines[i])
		l.pop(7)
		l.pop(4)
		arrayOfLines[i] = ''.join(l)
for i in range(153,160):
		l = list(arrayOfLines[i])
		l[4] = '0'
		l[6] = '0'
		arrayOfLines[i] = ''.join(l)
l = [-1]*24
for i in l:
		del arrayOfLines[i]

numberOfLines = len(arrayOfLines)
listFromLine= []
for line in arrayOfLines:
	listFromLine.append(line.split(','))

numberOfClass1 = 0
allString1 = []
for iter in listFromLine:
	if iter[1] not in allString1:
		numberOfClass1 +=1
		allString1.append(iter[1])

for iter in listFromLine:
	temp = allString1.index(iter[1])+1
	iter[1] = str(temp)

for iter in listFromLine:
	st = iter[2]
	stList = st.split('/')
	for i in range(2):
		l = list(stList[i])
		l.pop()
		l.pop()
		l.pop()
		stList[i] = ''.join(l)
	iter.pop(2)
	iter.insert(2,stList[0])
	iter.insert(3,stList[1])

numberOfClass3 = 0
allString3 = []
for iter in listFromLine:
	if iter[-1] not in allString3:
		numberOfClass3 +=1
		allString3.append(iter[-1])

for iter in listFromLine:
	temp = allString3.index(iter[-1])+1
	iter[-1] = str(temp)

out_path = os.path.join(parent_path, 'train_data')
fout = open(os.path.join(out_path, 'weather_feature_mat.txt'), 'w')
for iter in listFromLine:
	l = (','.join(iter))
	fout.write(''.join([l, '\n']))

fr.close()
fout.close()
