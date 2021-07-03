from itertools import combinations

vowels=('a','e','i','o','u')
n,m = map(int,input().split())
data=input().split()

#정렬된 암호
data.sort()
for password in combinations(data,n):
    count = 0
    for i in password:
        if i in vowels:
            count+=1
    if count>=1 and n-count >=2:
        print(''.join(password))