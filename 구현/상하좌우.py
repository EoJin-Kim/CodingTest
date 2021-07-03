n=int(input())

opers=list(input().split())
x,y=0,0
dx=[-1,0,1,0]
dy=[0,1,0,1]
def command(oper):
    result=-1
    if oper=="U":
        result=0
    elif oper=="R":
        result=1
    elif oper=="D":
        result=2
    else:
        result=3

    return result

for oper in opers:
    i=command(oper)
    nx = x+dx[i]
    ny= y+dy[i]
    if nx>=0 and nx <n and ny>=0 and ny<n:
        x = nx
        y= ny

print(x+1,y+1)
