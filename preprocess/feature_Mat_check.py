import os
def feature_Mat_check(filename, threshold):
    file_in = open(filename)
    array_of_lines =  file_in.readlines()
    list_of_lines = []
    for line in array_of_lines :
        temp = line.strip()
        temp = temp.split(' ')
        list_of_lines.append(temp)
    file_in.close()
    file_dir = os.path.dirname(filename)
    filename_out = os.path.join(file_dir, ''.join([filename, '_checked.txt'] ))
    file_out = open(filename_out, 'w')
    indexs = []
    for i in range(len(list_of_lines)) :
        if int(list_of_lines[i][5]) < threshold :
            indexs.append(i)
    indexs.sort(reverse = True)
    for i in indexs :
        del list_of_lines[i]
    for line in list_of_lines :
        out = ' '.join(line)
        file_out.write(''.join([out, '\n']))
    file_out.close()

parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_1 = os.path.join(data_path, 'featureMat_workday_line6.txt')
file_2 = os.path.join(data_path, 'featureMat_restday_line6.txt')
file_3 = os.path.join(data_path, 'featureMat_holiday_line6.txt')
file_4 = os.path.join(data_path, 'featureMat_workday_line11.txt')
file_5 = os.path.join(data_path, 'featureMat_restday_line11.txt')
file_6 = os.path.join(data_path, 'featureMat_holiday_line11.txt')
feature_Mat_check(file_1, 200)
feature_Mat_check(file_2, 200)
feature_Mat_check(file_3, 200)
feature_Mat_check(file_4, 400)
feature_Mat_check(file_5, 400)
feature_Mat_check(file_6, 400)
