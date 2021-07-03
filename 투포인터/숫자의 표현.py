def solution(n):
    array=[ i for i in range(1,n+1)]
    answer = 0
    start=0
    end=0
    while True:
        sumValue=sum(array[start:end+1])
        if sumValue==n:
            answer+=1
            start += 1
        elif sumValue>n:
            start+=1
        else:
            end+=1

        if start==n:
            break
    return answer

print(solution(15))