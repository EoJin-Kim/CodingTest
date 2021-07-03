def solution(citations):


    citations.sort(reverse=True)
    answer=1
    # 66, 22
    for i in range(len(citations)):


        if citations[i] < i+1:
            return i
    return len(citations)


print(solution([1545, 2, 999, 790, 540, 10, 22]))
print(solution([66, 22]))