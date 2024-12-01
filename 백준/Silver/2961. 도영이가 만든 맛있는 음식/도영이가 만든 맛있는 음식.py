n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
difference = float('inf')  # 신맛과 쓴맛의 차이

def dfs(idx, sourness, bitterness):
    global difference

    # 전체 탐색한 경우 종료
    if idx == n: return

    # 1. idx번째 재료 선택 안 하는 경우
    dfs(idx+1, sourness, bitterness)

    # 2. idx번째 재료 선택하는 경우
    sourness *= arr[idx][0]
    bitterness += arr[idx][1]
    difference = min(difference, abs(sourness - bitterness))

    dfs(idx+1, sourness, bitterness)

dfs(0, 1, 0)
print(difference)