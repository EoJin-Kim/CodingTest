
n=int(input())
# t는 상담을 완료하는데 걸리는 기간
t=[]
# p =[] 상담을 완료했을 때 받을 수 있는 금액
p=[]

# dp 테이블 초기화



for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

dp=[0] *(n+1)
max_value=0



for i in range(n-1,-1,-1):
    # 시간  = 현재 일의 시간 + 현재 일
    time = t[i] +i
    # time에서 (현재 일 -1) 이니까 부등호 <= 사용 (윈래 n+1)
    if time <=n:
        dp[i]=max(p[i] + dp[time],max_value)
        max_value=dp[i]

    else:
        dp[i]=max_value

print(max_value)

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
'''