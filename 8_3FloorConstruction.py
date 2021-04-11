n = int(input())

coverCount=[0]*1000
coverCount[1] =1
coverCount[2] = 3

for i in range(3,n+1):
    coverCount[i] =(coverCount[i-1]+coverCount[i-2]*2)%796796

print(coverCount[n])