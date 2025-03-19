def to_binary_iterative(n):
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2

    return result

def solution(s):
    count = 0  # 변환 횟수
    count_zero = 0  # 제거된 0의 개수

    while s != "1":
        count += 1  # 변환 횟수 증가
        count_zero += s.count('0')  # 제거된 0 개수 누적
        s = s.replace('0', '')  # 0 제거
        s = to_binary_iterative(len(s))  # 길이를 2진수로 변환

    return [count, count_zero]
