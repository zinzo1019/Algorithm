N, K = map(int, input().split())

result = 0
while N != 1:
    # 나누어떨어지면 나누기
    if N % K == 0:
        N //= K
    # 나누어떨어지지 않는다면 1 빼기
    else:
        N -= 1
    result += 1

print(result)