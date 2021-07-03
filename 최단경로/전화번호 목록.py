def solution(phone_book):
    answer = True
    #phone_book.sort(key=lambda x: len(x))
    phone_book.sort()
    print(phone_book)
    length=len(phone_book)

    for i in range(length-1):

        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True



print(solution([ "97674223","119", "1205524421"]))
print(solution(["123","456","789"]))