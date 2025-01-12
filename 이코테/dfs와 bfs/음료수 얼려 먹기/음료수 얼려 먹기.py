'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    # 범위를 벗어나면 종료
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    # 얼음이라면 탐색
    if not graph[y][x]:
        # 방문 처리
        graph[y][x] = 1
        # 4가지 방향으로 이동하면서 탐색
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    # 얼음이 아니라면 바로 거짓 리턴
    else:
        return False

result = 0
for x in range(m):
    for y in range(n):
        if dfs(x, y):
            result+=1

print(result)