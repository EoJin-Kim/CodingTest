data = input()

num=0
result=[]
for i in data:
    if i.isdigit():
        num+=int(i)
    else:
        result.append(i)


print(''.join(result),end='')
if num:
    print(num)