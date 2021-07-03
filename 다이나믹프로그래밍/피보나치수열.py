def solution(n):
    array=[0 for i in range(n+1)]
    array[1]=1
    array[2] = 1
    if n==1 or n==2:
        return 1
    for i in range(3,n+1):
        array[i]=array[i-1]+array[i-2]

    #print(array)
    return array[n]%1234567


print(solution(10))