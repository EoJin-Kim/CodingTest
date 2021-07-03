from bisect import bisect_left,bisect_right

array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

def CountRange(a,left,right):
    leftIndex = bisect_left(a,left)
    rightIndex = bisect_right(a,right)
    return rightIndex-leftIndex

def solution(words, queries):
    answer=[]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for ary in array:
        ary.sort()

    for ary in reversed_array:
        ary.sort()

    for query in queries:
        if query[0]!="?":
            answer.append(CountRange(array[len(query)],query.replace('?','a'),query.replace('?','z')))
        else:
            answer.append(CountRange(reversed_array[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z')))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))