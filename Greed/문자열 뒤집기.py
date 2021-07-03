data = input()

result1=0
result0=0
if data[0] =='0':
    result0+=1
else:
    result1+=1
for i in range(1,len(data)):
    if data[i]!=data[i-1]:
        if data[i]=='0':
            result0+=1
        else:
            result1+=1


print(min(result0,result1))


