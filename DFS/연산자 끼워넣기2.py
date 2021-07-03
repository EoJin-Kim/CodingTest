from itertools import permutations


n= int(input())

data=list(map(int,input().split()))
# + - x /
calc=["+","-","x","/"]
oper=list(map(int,input().split()))

command=""
for i in range(4):
    command+=calc[i]*oper[i]
command=list(command)

minValue=int(1e9)
maxValue=-int(1e9)
for comn in permutations(command,n-1):
    temp=data[0]
    for i in range(n-1):
        if comn[i]=="+":
            temp+=data[i+1]
        elif comn[i]=="-":
            temp-=data[i+1]
        elif comn[i]=="x":
            temp*=data[i+1]
        elif comn[i] == "/":
            temp = int(temp/data[i + 1])

    minValue=min(temp,minValue)
    maxValue=max(temp,maxValue)


print(maxValue)
print(minValue)



