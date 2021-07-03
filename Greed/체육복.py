

def solution(n, lost, reserve):
    answer = 0
    array=[0]*30
    for i in range(n):
        array[i]=1
    for i in lost:
        array[i-1]-=1

    for i in reserve:
        array[i-1]+=1
    [0,0,2,0,2]
    for i in range(n):
        if array[i]>1:
            if i - 1 >= 0 and array[i - 1] == 0:
                if array[i - 1] == 0 and array[i] > 1:
                    array[i - 1] = 1
                    array[i] = 1
            # 오른쪽이 0 인 경우
            if i+1<n and array[i + 1] == 0 :
                if array[i + 1] == 0 and array[i] > 1:
                    array[i + 1] = 1
                    array[i] = 1





    for i in array:
        if i:
            answer+=1
    #print(array)
    return answer
print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))