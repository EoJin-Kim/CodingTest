import copy
n = int(input())

array =list(map(int,input().split()))
array.sort()
'''
totalSet=set([0])
price=0
total = sum(array)
for i in array:
    #copy.deepcopy(totalSet)
    for j in list(totalSet):

        totalSet.add(j+i)
before = -1
for i in list(totalSet):
    if(before+1!=i):
        result = before +1
        break;
    else:
        before=i

print(result)
'''
target=1
print(array)
for x in array:
    if target<x:
        break
    else:
        target+=x
        #print(target)

print(target)




