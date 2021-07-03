from collections import deque

for tc in range(int(input())):
    n= int(input())
    indegree=[0]*(n+1)
    graph=[[False]*(n+1) for i in range(n+1)]

    #작년 순위
    data = list(map(int,input().split()))

    #방항그래프 간선 정보 초기화
    for i in range(n):
        for j in range(i+1,n):
            # 순위가 높으면 그래프 True 변경 i>j i가 순위가 높음
            graph[data[i]][data[j]]=True
            # 낮은 순위 indegree +=1
            indegree[data[j]]+=1

    #올해 변경된 순위
    m=int(input())
    for i in range(m):
        a,b = map(int,input().split())

        #간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1

        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1
    result=[]
    q=deque()

    #처음 시작할 때 진입차수가 0인것을 deque에 집어넣는다
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    certain =True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False #그래프 내 사이클이 존재하는지 여부


    for i in range(n):
        # 노드를 전부 확인하기전에 deque가 empty면 사이클 졵재
        if len(q)==0:
            cycle=True
            break
        #큐의 원소가 2개 이상이면 정렬 결과가 여러개라는 뜻
        if len(q)>=2:
            certain=False
        now=q.popleft()
        result.append(now)
        #모든 노드 for문
        for i in range(1,n+1):
            #현재 노드(now) 그래프에서 모든 노드(i) 검색하면서 True면 진입차수 1 감소
            if graph[now][i]:
                indegree[i]-=1
                # 진입차수가 0이면 큐에 추가
                if indegree[i]==0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i,end=" ")
        print()