import csv

data1=[]
data2=[]

with open('bright_stars.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        data1.append(row)

with open('cleaned.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        data2.append(row)

header1=data1[0]
header2=data2[0]

p_data1=data1[1:]
p_data2=data2[1:]

header=header1+header2

p_data=[]

for i in p_data1:
    p_data.append(i)

for i in p_data2:
    p_data.append(i)

print(p_data)
with open('total_stars.csv','w',encoding='utf8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(p_data)
