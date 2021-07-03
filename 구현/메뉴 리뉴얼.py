from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer=[]
    for crs in course:
        totalCounter={}
        for order in orders:
            tempCounter=Counter(combinations(order,crs))

            sortCounter = {}
            for key, value in tempCounter.items():
                sortCounter[''.join(sorted(key))]=value

            for key,value in sortCounter.items():
                if totalCounter.get(key):
                    totalCounter[key]+=1
                else:
                    totalCounter[key]=value
        maxValue=-1
        temp=[]
        for key, value in totalCounter.items():
            if value>maxValue:
                if value<=1:
                    continue
                temp=[key]
                maxValue=value
            elif value==maxValue:
                temp.append(key)

        for i in temp:
            answer.append("".join(i))
    answer.sort()
    #print(answer)

    return answer


#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABC", "DEF", "GHI"], [2, 3, 4]))
a=[]
a.append("")
print(a)