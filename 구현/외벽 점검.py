from itertools import permutations

def solution(n,weak,dist):
    length = len(weak)

    # weak 두배로 늘리기
    for i in range(length):
        weak.append(weak[i]+n)

    answer=len(dist)+1

    for start in range(length):
        for friends in permutations(dist,len(dist)):
            count =1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start]+friends[count-1]

            for index in range(start,start+length):
                if position < weak[index]:
                    count +=1
                    if count> len(dist):
                        break
                    position = weak[index] +friends[count-1]
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))