


def solution(s):
    answer =list(s)
    check=True


    for i in range(len(answer)):
        if answer[i].isalnum() and check==True:
            answer[i]=answer[i].upper()
            check=False

        elif answer[i].isalpha() and check==False:
            answer[i]=answer[i].lower()

        elif answer[i]==" ":
            check=True

    return "".join(answer)


print(solution(" 3people unFollowed me"))