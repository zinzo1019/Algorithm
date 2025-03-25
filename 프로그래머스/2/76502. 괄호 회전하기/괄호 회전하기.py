def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

def solution(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]  # 문자열 회전
        if is_valid(rotated_s):
            count += 1
    
    return count
