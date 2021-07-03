from collections import Counter

def solution(clothes):
    answer=1
    clotheCounter = Counter( b for a,b in clothes)
    for cnt in clotheCounter.values():
        answer = answer * (cnt+1)

    return answer-1





print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	))