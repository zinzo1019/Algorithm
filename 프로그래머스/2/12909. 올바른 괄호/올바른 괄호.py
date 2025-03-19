def solution(s):
    answer = True
    stack_arr = []

    for i in s:
        if i == "(":
            stack_arr.append("(")
        else:
            try:
                stack_arr.pop()
            except IndexError:
                answer = False

    if len(stack_arr) > 0:
        answer = False

    return answer
