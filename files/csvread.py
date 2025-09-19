import csv
f=open("file3.csv",'r')
rf=csv.reader(f)
for i in rf:
	print(i)
