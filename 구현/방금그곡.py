def solution(m, musicinfos):
    answer = [0, ""]
    music_dic = dict()
    m=m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for music in musicinfos:
        st, ed, title, sheet = music.split(",")
        sheet = sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        start = [int(time) for time in st.split(':')]
        end = [int(time) for time in ed.split(':')]
        all_time = (end[0] - start[0]) * 60 + (end[1] - start[1])
        sheet = sheet * (all_time // len(sheet)) + sheet[0:all_time % len(sheet)]
        music_dic[title] = sheet
        if m in sheet:
            if answer[0]<len(sheet):
                answer[0]=len(sheet)
                answer[1]=title
    if answer[0]!=0:
        return answer[1]
    else:
        return "(None)"
    '''
    for key, value in music_dic.items():
        if m in value:
            if len(answer[1]) < len(value):
                answer[0] = key
                answer[1] = value

    if len(answer[0]) == 0:
        return "(None)"
    else:
        return answer[0]
    '''





# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(	"CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
