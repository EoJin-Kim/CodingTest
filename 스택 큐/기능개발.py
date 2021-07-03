from collections import deque


def solution(progresses, speeds):
    pq = deque(progresses)
    sq = deque(speeds)
    answer = []
    while pq:
        count = 0
        print(pq)
        if pq[0] < 100:
            for i in range(len(pq)):
                pq[i] = pq[i] + sq[i]
        else:
            count=0
            while pq[0]>=100:
                count += 1
                pq.popleft()
                sq.popleft()
                if not pq:
                    break

        if count > 0:
            answer.append(count)

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))