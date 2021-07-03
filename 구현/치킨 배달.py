from itertools import combinations
n,m = map(int,input().split())
array=[]
INF=int(1e9)
for i in range(n):
    array.append(list(map(int,input().split())))

chick=[]
home=[]
for i in range(n):
    for j in range(n):
        if array[i][j]==2:
            chick.append((i,j))
        elif array[i][j]==1:
            home.append((i,j))



def chkDistance(home,chick):
    result=0
    temp=INF
    for h in home:
        temp = int(1e9)
        # 치킨 거리 구하기
        for c in chk:
            temp=min(temp,abs(c[0]-h[0])+abs(c[1]-h[1]))
        result+=temp
    return result
#치킨집 m개 선택
result=[]

for chk in combinations(chick,m):
    result.append(chkDistance(home,chk))
    #result=min(result,chkDistance(home,chk))

print(min(result))

