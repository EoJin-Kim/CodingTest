from collections import defaultdict

def solution(tickets):
    # 출발지가 키, 목적지가 value 인 딕셔너리 생성
    routes = defaultdict(list)
    for t in tickets:
        routes[t[0]].append(t[1])

    # 알파벳 빠른순으로 정렬해야함으로 reverse=True
    for r in routes:
        routes[r].sort(reverse=True)

    # 시작 위치 ICN
    stack = ['ICN']

    # 리턴 변수
    path = []

    while stack:
        # 현제 갈수 있는곳 찾기
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())

        # route 가 비지 않았는데 route[top]가 비어있다는것은 마지막 공항이라는 뜻
        else:
            path.append(stack.pop())


    # 마지막 공항을 찾기위해 path를 마지막에 역순 정렬렬
    return path[::-1]


print(soluiont([["ICN","BOO"],["ICN","COO"],["COO","ICN"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))