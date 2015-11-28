import os
##############################################################
#merge all holidays and restdays but national days

def merge(filename_1, filename_2, filename_3) :
    file_1 = open(filename_1)
    file_2 = open(filename_2)
    file_out = open(filename_out, )

parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_1 = os.path.join(data_path, 'featureMat_restday_line6.txt')
file_2 = os.path.join(data_path, 'featureMat_holiday_line6.txt')
file_3 = os.path.join(data_path, 'featureMat_restday_line11.txt')
file_4 = os.path.join(data_path, 'featureMat_holiday_line11.txt')