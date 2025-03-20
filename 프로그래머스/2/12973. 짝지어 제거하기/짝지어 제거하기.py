def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 같은 문자면 제거
        else:
            stack.append(char)  # 다른 문자면 추가

    return 1 if not stack else 0  # 스택이 비었으면 1, 아니면 0
