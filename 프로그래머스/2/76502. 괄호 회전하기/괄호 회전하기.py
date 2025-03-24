def solution(s):
    answer = 0

    # 필요한 괄호 세트 수
    necessary_couple_count = len(s) // 2
    # 카운트 된 괄호 세트 수
    couple_count = 0
    # s 배열의 두 배
    double_s = s * 2
    
    if len(s) % 2 != 0:
        return 0
    
    stack = []
    for start_index in range(0, len(s)):
        for i in range(start_index, start_index + len(s) + 1):
            if necessary_couple_count == couple_count:
                answer += 1
                couple_count = 0
                continue

            if double_s[i] in ["(", "{", "["]:
                stack.append(double_s[i])
            else:
                if not stack:
                    couple_count = 0
                    break
                else:
                    stack_pop = stack.pop()
                    if stack_pop + double_s[i] in ["()", "{}", "[]"]:
                        couple_count += 1

    return answer