from collections import deque

def bfs(graph, start, visited):
    queue = deque()

    # 시작 지점 방문 처리
    queue.append(start)
    visited[start] = True
    print(start, end=' ')

    # 큐가 빌 때까지 반복
    while queue:
        # 특정 지점과 연결된 지점들을 우선 방문 처리
        for i in graph[queue.popleft()]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

graph = [
	[],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
	[7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)