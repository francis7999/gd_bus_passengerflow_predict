#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import tree
import load_X_Y
from sklearn import preprocessing
import numpy as np

(X,y) = load_X_Y.load_X_Y('featureMat_restday_line10.txt_checked')

for item in X:
        for i in range(len(item)):
                item[i] = float(item[i])
                
                
X_scaled = preprocessing.scale(X)
clf = tree.DecisionTreeRegressor()
clf.fit(X_scaled, y)

n1 = len(X_scaled)
n2 = len(y)
if(n1 != n2):
	print '读取X和Y错误'

#全部样本拿来训练得到的训练集内错误率
numberOfError = 0
for n in range(n1):
	if(abs(y[n] - clf.predict(X_scaled[n])) >= 200):
		numberOfError +=1
		
print float(numberOfError)/float(n1)

for n in range(n1):
       print (list(X_scaled[n]),y[n],list(clf.predict(X_scaled[n])))

#k-flod cross validation
#numberOfError = 0
#k = 10
#clf.fit(X[0: n1/k*(k-1)],y[0: n1/k*(k-1)])
#for n in range(n1/k*(k-1), n1):
#        if(abs(y[n] - clf.predict(X[n])) >= 400):
#                numberOfError +=1
#                
#print float(numberOfError)/float(n1-n1/k*(k-1))

