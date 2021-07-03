


def PartSumCount(data,m):
    # 데이터 N의 개수
    n=len(data)
    count = 0
    interval_sum = 0
    end = 0
    for start in range(n):
        while interval_sum<m and end<n:
            interval_sum+=data[end]
            end+=1

        if interval_sum == m:
            count+=1

        interval_sum-=data[start]
    return count
m =5 #찾고자하는 부분합
data=[1,2,3,2,5]
print(PartSumCount(data,m))