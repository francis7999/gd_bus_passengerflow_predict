#!/usr/bin/python
# -*- coding: utf-8 -*-



import numpy as np

from sklearn import tree
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

import load_X_Y
import math
import os


###############################################################################
# Load data
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_in = os.path.join(data_path, 'featureMat_holiday_line6_checked.txt')
X,y = load_X_Y.load_X_Y(file_in)
X = np.array(X)
y = np.array(y)
rand_s = 700
X, y = shuffle(X, y, random_state=rand_s)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

fout = open('iteration.txt','w')
fout.write("min_samples_leaf\troot_of_mean_squaref_error_of_testset\n")
for m in range(1, 101):
    ###############################################################################
    # Fit regression model
    clf = tree.DecisionTreeRegressor(min_samples_leaf  = m)
    clf = clf.fit(X_train, y_train)

    mse = mean_squared_error(y_test, clf.predict(X_test))
    fout.write("%d\t%f\n" % (m, math.sqrt(mse)))
#    fout.write("min_samples_leaf: %d\n" % m)
#    fout.write("mean_squared_error_of_testset: %.4f \n" % mse)
#    fout.write("root_of_mean_squaref_error_of_testset: %.4f\n" % math.sqrt(mse))


fout.close()

