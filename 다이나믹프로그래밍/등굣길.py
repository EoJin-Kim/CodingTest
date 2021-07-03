

def solution(m, n, puddles):
    answer = 0
    if m==1 or n==1:
        return 1
    array=[[0] * m for i in range(n)]
    for py,px in puddles:
        array[px-1][py-1]=-1

    array[0][0]=1
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue

            if array[i][j]==-1:
                array[i][j]=0
                continue

            if i==0:
                array[i][j]=array[i][j-1]
            elif j==0:
                array[i][j]=array[i-1][j]
            else:
                array[i][j]=array[i-1][j]+array[i][j-1]
    return array[n-1][m-1]% 1000000007
print(solution(4,3,[[2, 2]]))
print(solution(4,3,[[2, 2]]))