import heapq

INF=int(1e9)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
tc=int(input())
for _ in range(tc):
    n=int(input())
    graph=[]
    distance=[[INF]*n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().split())))


    q=[]
    distance[0][0]=graph[0][0]
    heapq.heappush(q,(distance[0][0],0,0))
    while q:
        dist,x,y=heapq.heappop(q)
        if dist>distance[x][y]:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                cost =dist+graph[nx][ny]
                if cost<distance[nx][ny]:
                    distance[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))




    print(distance[n-1][n-1])


'''
1
3
5 5 4
3 9 1
3 2 7
'''