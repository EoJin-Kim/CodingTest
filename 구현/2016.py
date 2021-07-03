def solution(a, b):
    # 6
    result = 0
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        result += month[i]
    result += b
    result-=1
    answer = day[result % 7]

    # answer = ''
    return answer

print(solution(1,1))