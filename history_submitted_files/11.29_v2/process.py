import codecs

file_in  = open('GBDT_predict_data.txt')
out = []
for line in file_in:
    temp = line.strip()
    temp = temp.split(',')
    out.append(temp)

for line in out :
    if int(line[1]) <= 20150103 :
        num = int(line[3])
        num -= 20
        line[3] = str(num)

file_out = codecs.open('GBDT_predict_data2.txt', 'w', "utf-8")
for line in out :
    temp = ','.join(line)
    temp = ''.join([temp, '\r\n'])
    file_out.write(temp.decode('utf-8'))

file_in.close()
file_out.close()