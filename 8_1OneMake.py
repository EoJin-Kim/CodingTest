x=int(input())
array=[0]*30001




for i in range(2,30001):
    array[i]=array[i-1]+1

    if i%5==0:
        array[i]=min(array[i//5]+1,array[i])

    if i % 3 == 0:
        array[i] = min(array[i// 3] + 1,array[i])

    if i% 2 == 0:
        array[i] = min(array[i // 2] + 1,array[i])

print(array[x])
