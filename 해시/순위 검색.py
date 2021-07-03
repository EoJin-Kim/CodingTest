def solution(info, query):
    answer = []
    infoDic={}

    for i in info:
        a,b,c,d,e=i.split()
        if not infoDic.get(a):
            infoDic[a]={}
        if not infoDic[a].get(b):
            infoDic[a][b]={}
        if not infoDic[a][b].get(c):
            infoDic[a][b][c]={}
        if not infoDic[a][b][c].get(d):
            infoDic[a][b][c][d]=[]
        infoDic[a][b][c][d].append(e)

    for q in query:
        answer.append(infoDic,QueryCount(q))

    print(infoDic)
    return answer
def QueryCount(infoDic,q):
    #print(q)
    a,b,c,tmp=q.split(" and ")
    d,e=tmp.split(" ")
    print(a,b,c,d,e)
    findInfo = [[] for i in range(5)]
    print(findInfo)
    if a=="-":
        for keyA in infoDic.keys():
            findInfo[0].append(keyA)
    else:
        findInfo[0].append(a)
        if b == "-":
            for keyB in infoDic[a].keys():
            if c == "-":
                if d == "-":

    #print(a,b,c,d,e)
    return 1
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))