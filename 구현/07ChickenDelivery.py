from itertools import combinations
n,m = map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

house=[]
shop=[]

for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            house.append((i,j))
        elif data[i][j]==2:
            shop.append((i,j))



def get_sum(candidate):
    result=0
    # 집 하나 골라서
    for hx,hy in house:
        temp=1e9
        #조합 중에 치킨 거리가 가장 작은거 찾기
        for cx,cy in candidate:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

candidates = list(combinations(shop,m))
result=1e9
for candidate in candidates:
    result = min(get_sum(candidate),result)


print(result)

