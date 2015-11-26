#!/usr/bin/python
# -*- coding: utf-8 -*-


from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
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

clf = make_pipeline(PolynomialFeatures(4), Ridge())
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
       print (list(X[n]),list(X_scaled[n]),float(ulti_X[n]),y[n],list(clf.predict(ulti_X[n])))

#k-flod cross validation
#numberOfError = 0
#k = 10
#clf.fit(X[0: n1/k*(k-1)],y[0: n1/k*(k-1)])
#for n in range(n1/k*(k-1), n1):
#        if(abs(y[n] - clf.predict(X[n])) >= 400):
#                numberOfError +=1
#                
#print float(numberOfError)/float(n1-n1/k*(k-1))

fout1 = open('out1.txt','w')
for n in range(n1):
	fout1.write('\t'.join([str(float(ulti_X[n])),str(y[n]),'\n']))

fout1.close()

fout2 = open('out2.txt','w')
for n in range(n1):
	fout2.write('\t'.join([str(float(ulti_X[n])),str(float(clf.predict(ulti_X[n]))),'\n']))

fout2.close()
