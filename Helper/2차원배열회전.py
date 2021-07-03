# 시계 방향 회전
def Clock90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 반 시계 방향 회전
def ClockReverse90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[n-j-1][i] = a[i][j]
    return result

print(Clock90([[1,1,1],[2,2,2],[3,3,3]]))
print(ClockReverse90([[1,1,1],[2,2,2],[3,3,3]]))