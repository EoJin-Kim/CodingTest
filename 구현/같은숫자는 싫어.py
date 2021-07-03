def solution(arr):
    answer = []
    before=''
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if before!=i:
            answer.append(i)
        before=i

    return answer


print(solution(	[4, 4, 4, 3, 3]))