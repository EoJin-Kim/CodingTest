n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설취한 뒤의 맵 리스트

for i in range(n):
    data.append(list(map(int, input().split())))

# 방향 북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# DFS이용해 사방으로 퍼지기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] ==2:
                    virus(i,j)

        result = max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] ==0:
                data[i][j] =1
                count +=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)