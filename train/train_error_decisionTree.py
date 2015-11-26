#!/usr/bin/python
# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

import load_X_Y
import math


###############################################################################
# Load data
X,y = load_X_Y.load_X_Y('featureMat_workday_line10.txt_checked')
X = np.array(X)
y = np.array(y)
rand_s = 20
X, y = shuffle(X, y, random_state=rand_s)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

###############################################################################
# Fit regression model
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X_train, y_train)

mse = mean_squared_error(y_test, clf.predict(X_test))
print("mean_squared_error_of_testset: %.4f" % mse)
print("root_of_mean_squared_error_of_testset: %.4f" % math.sqrt(mse))


###############################################################################
# k-flod cross validation
numberOfError_train = 0
for n in range(len(X_train)):
    if abs(clf.predict(X_train[n]) - y_train[n]) >=200:
        numberOfError_train +=1
print "训练集错误率（阀值200）\n"
print float(numberOfError_train)/float(len(X_train))
print '\n'

numberOfError_test = 0
for n in range(len(X_test)):
    if abs(clf.predict(X_test[n]) - y_test[n]) >=200:
        numberOfError_test +=1
print "测试集错误率（阀值200）\n"
print float(numberOfError_test)/float(len(X_test))
print '\n'

fout1 = open('DT_out_training.txt','w')
fout1.write("训练集错误率（阀值200）\n")
fout1.write(str(float(numberOfError_train)/float(len(X_train))))
fout1.write('\n')
for n in range(len(X_train)):
    a = list(X_train[n])
    for i in range(len(a)):
        a[i] = str(a[i])
    c = list(clf.predict(X_train[n]))
    for i in range(len(c)):
        c[i] = str(c[i])

    fout1.write('\t'.join([''.join(a), str(y_train[n]), ''.join(c), '\n']))
fout1.close()
fout2 = open('DT_out_test.txt','w')
fout2.write("测试集错误率（阀值200）\n")
fout2.write(str(float(numberOfError_test)/float(len(X_test))))
fout2.write('\n')
for n in range(len(X_test)):
    a = list(X_test[n])
    for i in range(len(a)):
        a[i] = str(a[i])
    c = list(clf.predict(X_test[n]))
    for i in range(len(c)):
        c[i] = str(c[i])

    fout2.write('\t'.join([''.join(a), str(y_test[n]), ''.join(c), '\n']))
fout2.close()
###############################################################################
# Plot feature importance
feature_importance = clf.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
a = np.array(['interval', 'weather', 'temp_high', 'temp_low', 'wind'])
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 1, 1)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, a[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()

