#!/usr/bin/python
# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

import load_X_Y
import math
import os
###############################################################################
# Load data
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
file_in = os.path.join(data_path, 'featureMat_restday_line6_checked.txt')
X,y = load_X_Y.load_X_Y(file_in)
X = np.array(X)
y = np.array(y)
rand_s = 400
X, y = shuffle(X, y, random_state=rand_s)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

###############################################################################
# Fit regression model|
params = {'n_estimators':1500, 'max_depth': 3, 'min_samples_split': 1,
          'learning_rate': 0.005, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(X_train, y_train)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("mean_squared_error_of_testset: %.4f" % mse)
print("root_of_mean_squared_error_of_testset: %.4f" % math.sqrt(mse))
print("random_state: %d, n_estimators： %d, max_depth: %d, min_samples_split: %d, learning_rate: %d, loss_func: %s" % (rand_s, params['n_estimators'],  params['max_depth'],  params['min_samples_split'],  params['learning_rate'],  params['loss']))

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

fout1 = open('GBDT_out_training.txt','w')
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
fout2 = open('GBDT_out_test.txt','w')
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
# Plot training deviance

# compute test set deviance
test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

for i, y_pred in enumerate(clf.staged_predict(X_test)):
    test_score[i] = clf.loss_(y_test, y_pred)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')

###############################################################################
# Plot feature importance
feature_importance = clf.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
a = np.array(['interval', 'weather', 'temp_high', 'temp_low', 'wind'])
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 2, 2)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, a[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
