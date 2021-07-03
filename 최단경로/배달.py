import heapq
INF=int(1e9)


def solution(N, road, K):
    answer = 0
    distance = [INF for i in range(N+1)]
    graph=[[] for i in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a, c))
    q=[]
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost =dist+i[1]
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    #print(distance)
    for i in distance:
        if i<=K:
            answer+=1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))