str ="surya"
vowels="aeiou"
count=0;
c=0;
for i in str:
    if i in vowels:
        count+=1;
    else:
        c+=1;
print("no:of vowels in ",str,"is",count);
print("no:of consonents in ",str,"is",c);
