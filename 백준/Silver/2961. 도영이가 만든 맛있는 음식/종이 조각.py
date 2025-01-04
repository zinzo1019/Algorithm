# 입력 받기
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

def dfs(n, m, arr):
    max_total_sum = 0

    # 모든 비트 상태 탐색 (0: 가로, 1: 세로)
    for state in range(1 << (n * m)):
        total_sum = 0

        # 가로 조각 계산
        for i in range(n):
            row_num = 0
            for j in range(m):
                if not (state & (1 << (i * m + j))):
                    row_num = row_num * 10 + arr[i][j]
                else:
                    total_sum += row_num
                    row_num = 0
            total_sum += row_num

        # 세로 조각 계산
        for j in range(m):
            col_num = 0
            for i in range(n):
                if state & (1 << (i * m + j)):
                    col_num = col_num * 10 + arr[i][j]
                else:
                    total_sum += col_num
                    col_num = 0
            total_sum += col_num

        max_total_sum = max(max_total_sum, total_sum)

    return max_total_sum

# 최대 조각 합 출력
print(dfs(n, m, arr))
