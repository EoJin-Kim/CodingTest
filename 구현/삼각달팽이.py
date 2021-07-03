def solution(n):
    answer = []
    dx=[1,0,-1]
    dy=[0,1,-1]
    direction=0
    array=[[0]*i for i in range(1,n+1)]
    x,y=-1,0
    idx=0
    for i in range(n,0,-1):
        for _ in range(i):
            x=x+dx[direction]
            y=y+dy[direction]
            idx+=1
            array[x][y]=idx
        direction=(direction+1)%3
    for i in array:
        answer.extend(i)
    return answer


print(solution(4))
print(solution(1))
print(solution(2))
#print(solution(4))