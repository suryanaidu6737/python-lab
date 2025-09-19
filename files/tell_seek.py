f=open("file1.txt",'r')
print("initial cursor position",f.tell())
print(f.read())
print("end cursor position",f.tell())
f.seek(12)
print("after seek(12) current cursor position",f.tell())
print("reading from cursor position")
print(f.read())


