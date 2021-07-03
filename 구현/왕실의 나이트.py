oper=['a','b','c','d','e','f','g','h']
pos=input()
x=int(pos[1])-1
y=int(oper.index(pos[0]))




moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(1,-2),(-1,-2)]
result=0
for move in moves:
    nx=x+move[0]
    ny=y+move[1]

    if nx>=0 and nx<8 and ny>=0 and ny<8:
        result+=1

print(result)