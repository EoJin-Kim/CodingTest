# 모든 삭제작업시 NULL 체크 필수!!

def solution(new_id):
    answer = ''

    # 1단계
    modifyID = new_id.lower()

    # 2단계
    tempID=""
    for i in modifyID:
        if i.isalpha() or i.isdigit() or i=="-" or i=="_" or i==".":
            tempID+=i
    modifyID=tempID

    # 3단계
    while True:
        #print(modifyID.find(".."))
        if modifyID.find("..")!=-1:
            modifyID = modifyID.replace("..",".")
        else:
            break
    # 4단계
    if modifyID:
        if modifyID[0]==".":
            modifyID=modifyID[1:]

    if modifyID:
        if modifyID[-1]==".":
            modifyID = modifyID[:-1]

    #5단계
    if modifyID=="":
        modifyID+="a"

    # 6단계
    length = len(modifyID)
    if length>=16:
        modifyID=modifyID[:15]
        if modifyID[0] == ".":
            modifyID = modifyID[1:]
        if modifyID[-1] == ".":
            modifyID = modifyID[:-1]

    # 7단계

    while len(modifyID)<=2:
        modifyID+=modifyID[-1]

    return modifyID



#print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("z-+.^."))
print(solution("=.="))