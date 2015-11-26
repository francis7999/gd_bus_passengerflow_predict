#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import neighbors
import load_X_Y
from sklearn import preprocessing
import numpy as np

(X,y) = load_X_Y.load_X_Y('featureMat_restday_line10.txt_checked')

for item in X:
        for i in range(len(item)):
                item[i] = float(item[i])
                
                
X_scaled = preprocessing.scale(X)
mat_X_scaled =  np.matrix(X_scaled)
weights = np.matrix([0.88181899, 0.03112526, 0.04583346, 0.02779611, 0.01342619])
weights = weights.transpose()
ulti_X = np.array(mat_X_scaled*weights)

clf = neighbors.KNeighborsRegressor(1)
clf.fit(ulti_X, y)

n1 = len(ulti_X)
n2 = len(y)
if(n1 != n2):
	print '读取X和Y错误'

#全部样本拿来训练得到的训练集内错误率
numberOfError = 0
for n in range(n1):
	if(abs(y[n] - clf.predict(ulti_X[n])) >= 200):
		numberOfError +=1
		
print float(numberOfError)/float(n1)

for n in range(n1):
       print (list(X_scaled[n]),list(ulti_X[n]),y[n],list(clf.predict(ulti_X[n])))

#k-flod cross validation
numberOfError = 0
k = 10
clf.fit(ulti_X[0: n1/k*(k-1)],y[0: n1/k*(k-1)])
for n in range(n1/k*(k-1), n1):
        if(abs(y[n] - clf.predict(ulti_X[n])) >= 400):
                numberOfError +=1
                
print float(numberOfError)/float(n1-n1/k*(k-1))

for n in range(n1/k*(k-1), n1):
       print (list(X_scaled[n]),list(ulti_X[n]),y[n],list(clf.predict(ulti_X[n])))

