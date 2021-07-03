def solution(land):
    answer = 0
    row=len(land)
    col=len(land[0])
    for i in range(1,row):
        for j in range(col):
            temp=land[i-1].copy()
            temp.pop(j)
            maxValue=max(temp)
            land[i][j]=maxValue+land[i][j]




    return max(land[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))