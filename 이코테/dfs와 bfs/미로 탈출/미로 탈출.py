'''
5 6
101010
111111
000001
111111
111111
'''

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        # 탐색 기준 좌표
        x, y = queue.pop()

        # 네 방향 탐색
        for i in range(4):

            # 다음 탐색 좌표
            ny = y + dy[i]
            nx = x + dx[i]

            # 영역을 벗어남
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            # 괴물이 존재함
            if graph[ny][nx] == 0:
                continue
            # 탐색 완료
            if graph[ny][nx] > 1:
                continue

            # 최단 거리 업데이트
            graph[ny][nx] = graph[y][x] + 1
            # 새로운 탐색 기준 좌표 삽입
            queue.append((nx, ny))
        print(graph[n - 1][m - 1])

bfs(0, 0)