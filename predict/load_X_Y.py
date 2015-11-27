#!/usr/bin/python
# -*- coding: utf-8 -*-


def load_X_Y(filename):
	fr = open(filename)
	arrayOfLines = fr.readlines()
	listFromLine= []
	for line in arrayOfLines:
			line = line.strip()
			listFromLine.append(line.split(' '))

	for iter in listFromLine:
		for i in range(len(iter)):
			iter[i] = int(iter[i])

	X = []
	y = []
	for iter in listFromLine:
		X.append(iter[0:5])
		y.append(iter[-1])

	return (X,y)

