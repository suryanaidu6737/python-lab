import csv
info=[['id','name'],[1,'surya'],[2,'syam'],[3,'harish']]
f=open('file3.csv','w',newline="")
wf=csv.writer(f)
wf.writerows(info)
