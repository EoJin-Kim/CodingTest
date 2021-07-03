# 사전에 정령된 리스트 A와 B 선언
a = [1,3,5]
b = [2,4,6,8]

def list_sum(a,b):
    n,m=len(a),len(b)
    result = [0] * (n + m)
    i,j,k=0,0,0
    while i<n or j<m:
        #a원소가 더 적을 경우
        if j>= m or(i<n and a[i] <=b[j]):
            result[k]=a[i]
            i+=1
        else:
            result[k] = b[j]
            j+=1
        k+=1
    return result

result = list_sum(a,b)
for i in result:
    print(i,end=' ')