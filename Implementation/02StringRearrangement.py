data = list(input())
String=[]
Num=0
for i in data:
    if i.isalpha():
        String.append(i)
    else:
        Num+=int(i)
String=sorted(String)
if Num!=0:
    String.append(str(Num))

print(''.join(String))
