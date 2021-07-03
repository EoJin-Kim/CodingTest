

prefix_sum=[0]
def SectionSum(data):
    n=len(data)
    sum_value = 0

    for i in data:
        sum_value+=i
        prefix_sum.append(sum_value)

left=3
right=4
data=[10,20,30,40,50]
SectionSum(data)
# 중요 !! left 포함이니까 left-1 인덱스 뺴주기
print(prefix_sum[right]-prefix_sum[left-1])