import sys
input = sys.stdin.readline

n,c = map(int,input().split())
array=[]
for i in range(n):
    array.append(int(input()))

array.sort()
#최소 거리 차이 (1보단 작을 수 없음)
start = 1
# 최대 거리 차이 (끝에서 처음 빼기)
end = array[-1] - array[0]
result=0

while start<=end:
    mid=(start+end)//2
    value=array[0]
    count=1
    # 0번 인덱스에 공유기 설치 했으므로 1부터 시작
    for i in range(1,n):
        # 설치되어있는 집부터 mid 거리보다 이상이면 설치
        if array[i]>=value+mid:
            value = array[i]
            count+=1

    # 공유기 개수가 같거나 많으면 거리를 줄일수 있는지 체크
    if count >= c:
        start = mid+1
        result = mid

    else:
        end = mid-1
print(result)
'''
5 3
1
2
8
4
9
'''