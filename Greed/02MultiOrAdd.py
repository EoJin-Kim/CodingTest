array=input()
result=int(array[0])
before=array[0]
for i in array[1:]:

    if before =='0' or before=='1':
        result+=int(i)
    else:
        result*=int(i)
    before=int(i)

print(result)