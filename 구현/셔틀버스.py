def solution(n, t, m, timetable):
    ttable = []
    # timetable 분으로 바꾸기
    for tt in timetable:
        hour, minute = map(int, tt.split(":"))
        ttable.append(hour * 60 + minute)

    ttable.sort()
    busTimeList = []
    busTimeDict = {}
    # 첫차는 9시 차니까 60*9
    busTimeList.append(540)
    busTimeDict[540] = []
    busTime = 540

    # 버스 시간표 딕셔너리
    for i in range(n - 1):
        busTime += t
        busTimeList.append(busTime)
        busTimeDict[busTime] = []

    # 사람을 태울 버스 위치
    busIdx = 0

    # 사람 버스에 순서대로 태우기
    for x in ttable:
        # 버스 시간표 인덱스를 초과하면 break
        if busIdx >= len(busTimeList):
            break

        # 버스당 좌석이 가득차면 busIdx 증가
        if len(busTimeDict[busTimeList[busIdx]]) >= m:
            busIdx += 1
            if busIdx >= len(busTimeList):
                break

        check = False
        # 늦게와서 현재 busIdx를 탑승하지 못하는 경우
        while busIdx < len(busTimeList):
            # 다음 버스 승차
            if x > busTimeList[busIdx]:
                busIdx += 1

            # 모든 버스를 못 타는 경우
            else:
                check = True
                break

        # 사람은 남았는데 버스 시간이 없는 경우 break
        if not check:
            break

        # 해당 시간버스에 탑승 가능한 경우
        busTimeDict[busTimeList[busIdx]].append(x)

    # 마지막 버스 시간이 남은 경우
    if len(busTimeDict[busTimeList[-1]]) < m:
        answer = busTimeList[-1]

    # 마지막 버스시간대에 사람이 가득 차 있는 경우
    else:
        answer = busTimeDict[busTimeList[-1]][-1] - 1
    return '{0:02d}:{1:02d}'.format(answer // 60, answer % 60)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
