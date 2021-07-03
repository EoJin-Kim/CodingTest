from collections import deque


def solution(priorities, location):
    array = []
    for i in range(len(priorities)):
        array.append((priorities[i],i))
    q = deque(array)
    answer = 0
    while q:
        first = q.popleft()
        count=0
        for i in range(len(q)):
            if first[0] < q[i][0]:
                q.append(first)
                break
            else:
                count+=1
        if count==len(q):
            answer+=1
            if first[1]==location:
                return answer

print(solution([2,1,3,2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
print(solution([1, 2,3,4],0))
print(solution([4,3,2, 1],0))