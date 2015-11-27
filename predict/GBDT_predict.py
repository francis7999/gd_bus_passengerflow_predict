#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import ensemble
from sklearn.utils import shuffle
import load_X_Y
import codecs
import os

def preprocess (filename):
    X,y = load_X_Y.load_X_Y(filename)
    X = np.array(X)
    y = np.array(y)
    rand_s = 20
    X, y = shuffle(X, y, random_state=rand_s)
    return (X, y)

fout = codecs.open('GBDT_predict_data.txt', 'w', "utf-8")
###############################################################################
# Load data
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file1_in = os.path.join(data_path, 'featureMat_workday_line6_checked.txt')
file2_in = os.path.join(data_path, 'featureMat_restday_line6_checked.txt')
file4_in = os.path.join(data_path, 'featureMat_workday_line11_checked.txt')
file5_in = os.path.join(data_path, 'featureMat_restday_line11_checked.txt')
X1, y1 = preprocess(file1_in)
X2, y2 = preprocess(file2_in)
X4, y4 = preprocess(file4_in)
X5, y5 = preprocess(file5_in)
work_weather = [[3, 23, 14, 1],
                [16, 23, 17, 1],
                [23, 24, 14, 6],
                [3, 17, 10, 8]]

rest_weather = [[10, 19, 6, 1],
                [10, 20, 7, 1],
                [10, 21, 8, 1]]

###############################################################################
# Fit regression model|
params1 = {'n_estimators':1500, 'max_depth': 3, 'min_samples_split': 1,
          'learning_rate': 0.005, 'loss': 'ls'}
params2 = {'n_estimators':1500, 'max_depth': 3, 'min_samples_split': 1,
          'learning_rate': 0.005, 'loss': 'ls'}
params4 ={'n_estimators':1500, 'max_depth': 3, 'min_samples_split': 1,
          'learning_rate': 0.005, 'loss': 'ls'}
params5 = {'n_estimators':1500, 'max_depth': 3, 'min_samples_split': 1,
          'learning_rate': 0.005, 'loss': 'ls'}
clf1 = ensemble.GradientBoostingRegressor(**params1)
clf2 = ensemble.GradientBoostingRegressor(**params2)
clf4 = ensemble.GradientBoostingRegressor(**params4)
clf5 = ensemble.GradientBoostingRegressor(**params5)
clf1.fit(X1, y1)
clf2.fit(X2, y2)
clf4.fit(X4, y4)
clf5.fit(X5, y5)

###############################################################################
# Predict new data
for w in work_weather:
    for i in range(6, 22, 1):
        p = [i, w[0], w[1], w[2], w[3]]
        b = list('2015010')
        b.append(str(work_weather.index(w) + 4))
        c = ''.join(b)
        a1 = clf1.predict(p)
        if i<10 :
            out1 = ','.join([u'线路6', c, ''.join(['0',str(i)]), str(int(a1[0]))])
        else:
            out1 = ','.join([u'线路6', c, str(i), str(int(a1[0]))])
        a4 = clf4.predict(p)
        if i<10 :
            out2 = ','.join([u'线路11', c, ''.join(['0',str(i)]), str(int(a4[0]))])
        else:
            out2 = ','.join([u'线路11', c, str(i), str(int(a4[0]))])
        out1 = ''.join([out1, '\r\n' ])
        out2 = ''.join([out2, '\r\n' ])
        fout.write(out1)
        fout.write(out2)

for w in rest_weather:
    for i in range(6, 22, 1):
        p = [i, w[0], w[1], w[2], w[3]]
        b = list('2015010')
        b.append(str(rest_weather.index(w) + 1))
        c = ''.join(b)
        a2= clf2.predict(p)
        if i<10 :
            out1 = ','.join([u'线路6', c, ''.join(['0',str(i)]), str(int(a2[0]))])
        else:
            out1 = ','.join([u'线路6', c, str(i), str(int(a2[0]))])
        a5 = clf5.predict(p)
        if i<10 :
            out2 = ','.join([u'线路11', c, ''.join(['0',str(i)]), str(int(a5[0]))])
        else:
            out2 = ','.join([u'线路11', c, str(i), str(int(a5[0]))])
        out1 = ''.join([out1, '\r\n' ])
        out2 = ''.join([out2, '\r\n' ])
        fout.write(out1)
        fout.write(out2)
fout.close()


