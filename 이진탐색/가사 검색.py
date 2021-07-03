from bisect import bisect_left,bisect_right

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        # 접미사에 와일드 카드가 붙은 경우
        if q[0] !='?':
            res = count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))


        # 접두사에 와일드 카드가 붙은경우
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        answer.append(res)
    return answer

def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_indext=bisect_left(a,left_value)
    return right_index-left_indext

array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))