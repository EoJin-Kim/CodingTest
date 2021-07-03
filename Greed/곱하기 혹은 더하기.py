data=input()
result=0
for i in data:
    if i=='0' or i=='1' or result==0:
        result+=int(i)

    else:
        result*=int(i)


print(result)