def solution(n):
    answer = 0

    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break  # 찾았으면 더 이상 진행할 필요 없음
            elif sum > n:
                break  # n을 초과하면 중단

    return answer
