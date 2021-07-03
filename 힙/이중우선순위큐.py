import sys
import heapq

def solution(operations):
    answer = []

    minHeapq = []
    maxHeapq = []
    visited = [False] * 1000001
    for i in range(len(operations)):
        command, num = operations[i].split()
        num = int(num)
        if command == "I":
            heapq.heappush(minHeapq, (num,i))
            heapq.heappush(maxHeapq, (-num,i))
            visited[i]=True
        else:
            if num == 1 and maxHeapq:
                while maxHeapq and visited[maxHeapq[0][1]]==False:
                    heapq.heappop(maxHeapq)
                if maxHeapq:
                    tmp =heapq.heappop(maxHeapq)
                    visited[tmp[1]] = False

            elif num == -1 and minHeapq:
                while minHeapq and visited[minHeapq[0][1]]==False:
                    heapq.heappop(minHeapq)
                if minHeapq:
                    tmp = heapq.heappop(minHeapq)
                    visited[tmp[1]] = False

    while maxHeapq and visited[maxHeapq[0][1]] == False:
        heapq.heappop(maxHeapq)

    while minHeapq and visited[minHeapq[0][1]] == False:
        heapq.heappop(minHeapq)

    if maxHeapq and minHeapq:
        return [-maxHeapq[0][0],minHeapq[0][0]]

    else:
        return [0,0]




print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))

'''
        maxSet = set(maxHeapq)
        minList = [ -x for x in minHeapq]
        minSet = set(minHeapq)
        result =minSet & maxSet

        if not result:
            print("EMPTY")
            continue
        print(lastMax,lastMin)
'''

'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333

'''