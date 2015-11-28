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
file_in = os.path.join(data_path, 'featureMat_merge_rest_line11.txt')
X,y = load_X_Y.load_X_Y(file_in)
X = np.array(X)
y = np.array(y)

fout = open('iteration.txt','w')
fout.write("min_samples_leaf\troot_of_mse_of_testset\ttrain_error_rate\ttest_error_rate\n")
for m in range(1, 101):
    X_train_array = list()
    y_train_array = list()
    X_test_array = list()
    y_test_array = list()
    mse_s = list()
    train_error_rates = list()
    test_error_rates = list()
    for rand_s in [10, 50, 100, 300, 500, 900, 1400, 4500, 3400, 22] :
        ###############################################################################
        # 10_fold randomly assign
        X, y = shuffle(X, y, random_state=rand_s)
        X = X.astype(np.float32)
        offset = int(X.shape[0] * 0.9)
        X_train, y_train = X[:offset], y[:offset]
        X_test, y_test = X[offset:], y[offset:]
        X_train_array.append(X_train)
        y_train_array.append(y_train)
        X_test_array.append(X_test)
        y_test_array.append(y_test)
        ###############################################################################
        # Fit regression model
        clf = tree.DecisionTreeRegressor(min_samples_leaf  = m)
        clf.fit(X_train, y_train)
        ###############################################################################
        # mean squared error
        mse = mean_squared_error(y_test, clf.predict(X_test))
        mse_s.append(mse)
        ###############################################################################
        # 10-flod cross validation
        numberOfError_train = 0
        for n in range(len(X_train)):
            if abs(clf.predict(X_train[n]) - y_train[n]) >=200:
                numberOfError_train +=1
        train_error_rates.append(float(numberOfError_train)/float(len(X_train)))
        numberOfError_test = 0
        for n in range(len(X_test)):
            if abs(clf.predict(X_test[n]) - y_test[n]) >=200:
                numberOfError_test +=1
        test_error_rates.append(float(numberOfError_test)/float(len(X_test)))
    mse_s = np.array(mse_s)
    fout.write("%d\t%f\t" % (m, math.sqrt(mse_s.mean())))
    #################################################################################
    #output mean of train error rates
    train_error_rates = np.array(train_error_rates)
    fout.write("%f\t" % train_error_rates.mean())
    #################################################################################
    #output mean of test error rates
    test_error_rates = np.array(test_error_rates)
    fout.write("%f\n" % test_error_rates.mean())

#    fout.write("min_samples_leaf: %d\n" % m)
#    fout.write("mean_squared_error_of_testset: %.4f \n" % mse)
#    fout.write("root_of_mean_squaref_error_of_testset: %.4f\n" % math.sqrt(mse))


fout.close()
