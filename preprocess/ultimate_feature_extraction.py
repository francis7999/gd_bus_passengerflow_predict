def ultimate_feature_extraction(file_input1, file_input2, file_Output):
	fr1 = open(file_input1)
	fr2 = open(file_input2)
	fout = open(file_Output,'w')
	arrayOfLines1 = fr1.readlines()
	listFromLine1= []
	for line in arrayOfLines1:
			line = line.strip()
			listFromLine1.append(line.split(' '))

	arrayOfLines2 = fr2.readlines()
	listFromLine2= []
	for line in arrayOfLines2:
	        line = line.strip()
	        listFromLine2.append(line.split(','))

	featureList = []
	for iter1 in listFromLine1:
		for iter2 in listFromLine2:
			if iter2[0].find(iter1[0])>-1:
				tempList = [iter2[0], iter1[1], iter1[2], iter1[3], iter1[4], iter2[1]]
				featureList.append(tempList)

	for iter in featureList:
	        l = list(iter[0])
	        l = l[-2:]
	        iter[0] = ''.join(l)
	        iter.append('\n')
	        OutputString = ' '.join(iter)
	        fout.write(OutputString)

	fr1.close()
	fr2.close()
	fout.close()
