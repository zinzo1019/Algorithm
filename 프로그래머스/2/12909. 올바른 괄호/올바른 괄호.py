def solution(s):
    answer = True

    count_open = 0
    count_close = 0

    for i in s:
        if i == "(":
            count_open += 1
        else :
            count_close += 1

        if count_open < count_close:
            answer = False
    
    if count_open != count_close:
        answer = False
    if s[len(s)-1] != ")":
        answer = False

    return answer
