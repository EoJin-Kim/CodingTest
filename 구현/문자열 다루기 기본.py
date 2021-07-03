def solution(s):
    length = len(s)

    if length == 4 or length == 6 :
        if s.isdigit():
            return True

    a=[1,2,3,4]
    print(a.find(1))
    return False



print(solution("a234"))