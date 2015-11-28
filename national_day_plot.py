import os
import matplotlib.pyplot as plt
cur_path = os.getcwd()
data_path = os.path.join(cur_path, 'train_data')
workday_file = open(os.path.join(data_path, 'workday.txt'))
holiday_file = open(os.path.join(data_path, 'holiday.txt'))
restday_file = open(os.path.join(data_path, 'restday.txt'))
line6_file = open(os.path.join(data_path, 'line6_stat.txt'))
line11_file = open(os.path.join(data_path, 'line11_stat.txt'))
workday_lines= workday_file.readlines()
workday_list= []
for line in workday_lines :
    line = line.strip()
    workday_list.append(line)
holiday_lines= holiday_file.readlines()
holiday_list= []
for line in holiday_lines :
    line = line.strip()
    holiday_list.append(line)
restday_lines= restday_file.readlines()
restday_list= []
for line in restday_lines :
    line = line.strip()
    restday_list.append(line)
line6_lines= line6_file.readlines()
line6_list= []
for line in line6_lines :
    line = line.strip()
    line = line.split(',')
    line6_list.append(line)
line11_lines= line11_file.readlines()
line11_list= []
for line in line11_lines :
    line = line.strip()
    line = line.split(',')
    line11_list.append(line)



for i in holiday_list :
    x1 = []
    y1 = []
    for j in line6_list:
        if i in j[0] :
            x1.append(int(j[0][-2:]))
            y1.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x1, y1, '--o')
    plt.xlabel(''.join([i, '_line6']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join(['line6_holi_', i, '.png']), dpi = 72)
    x2 = []
    y2 = []
    for j in line11_list:
        if i in j[0] :
            x2.append(int(j[0][-2:]))
            y2.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x2, y2, '--o')
    plt.xlabel(''.join([i, '_line11']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join(['line11_holi_', i, '.png']), dpi = 72)

for i in restday_list :
    x1 = []
    y1 = []
    for j in line6_list:
        if i in j[0] :
            x1.append(int(j[0][-2:]))
            y1.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x1, y1, '--o')
    plt.xlabel(''.join([i, '_line6']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join(['line6_rest_', i, '.png']), dpi = 72)
    x2 = []
    y2 = []
    for j in line11_list:
        if i in j[0] :
            x2.append(int(j[0][-2:]))
            y2.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x2, y2, '--o')
    plt.xlabel(''.join([i, '_line11']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join([ 'line11_rest_', i, '.png']), dpi = 72)

for i in workday_list :
    x1 = []
    y1 = []
    for j in line6_list:
        if i in j[0] :
            x1.append(int(j[0][-2:]))
            y1.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x1, y1, '--o')
    plt.xlabel(''.join([i, '_line6']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join(['line6_work_', i, '.png']), dpi = 72)
    x2 = []
    y2 = []
    for j in line11_list:
        if i in j[0] :
            x2.append(int(j[0][-2:]))
            y2.append(int(j[1]))
    plt.figure(figsize = (10,7))
    plt.subplot(1,1,1)
    plt.plot(x2, y2, '--o')
    plt.xlabel(''.join([i, '_line11']))
    plt.ylabel('passenger flow')
    plt.savefig(''.join([ 'line11_work_', i, '.png']), dpi = 72)
