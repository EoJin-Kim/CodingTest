import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

dx=[-1,0,1,0]
dy=[0,1,0,-1]


result=[]

for tc in range(int(input())):
    n=int(input())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))

    distance=[[INF] * n for _ in range(n)]
    x,y=0,0
    q=[(graph[x][y],x,y)]
    distance[x][y]=graph[x][y]
    while q:
        dist,x,y=heapq.heappop(q)
        # dist가 더 크다는 건 distancer INF로 초기화 했는데 INF가 아니니까 처리된적 있다는 뜻
        if dist>distance[x][y]:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and nx <n and ny>=0 and ny<n:
                cost = dist + graph[nx][ny]
                # 최소비용으로 nx, ny 설정
                if cost < distance[nx][ny]:
                    distance[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))


    print(distance[n-1][n-1])

