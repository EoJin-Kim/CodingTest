from collections import deque


def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        return len(cities)*5
    cache=deque(["" for i in range(cacheSize)])
    #print(cache)
    #c=["Jeju", "Pangyo", "Seoul"]
    for x in cities:
        if not x.lower() in cache:
            cache.popleft()
            cache.append(x.lower())
            answer+=5
        else:
            #idx=cache.index(x.lower())
            cache.remove(x.lower())
            cache.append(x.lower())
            answer+=1
    return answer
#print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
#print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
#print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution( 5,["SEOUL", "SEOUL", "SEOUL"]))