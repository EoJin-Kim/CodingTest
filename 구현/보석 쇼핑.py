# 투 포인터로 풀면된다
def solution(gems):
    answer = []
    length=len(gems)

    jewelryCount=len(set(gems))
    start=0
    end=0
    count=len(gems)+1
    dict={}
    while end<length:
        # 딕셔너리로 카운트 하기
        # value가 0이면 키 삭제
        if len(dict)==jewelryCount:
            dict[gems[start]]-=1
            if dict[gems[start]]==0:
                del dict[gems[start]]
            start+=1

        else:
            dict[gems[end]]=dict.get(gems[end],0)+1
            #if end!=length-1:
            end+=1

        if len(dict) == jewelryCount:
            if count > end - start:
                answer = [start + 1, end]
                count = end - start
    while True:
        if start==length-1:
            break

        dict[gems[start]] -= 1
        if dict[gems[start]] == 0:
            del dict[gems[start]]
        start += 1
        if len(dict)==jewelryCount:
            answer = [start + 1, end]
        else:
            break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution( ["A", "A", "B"]))