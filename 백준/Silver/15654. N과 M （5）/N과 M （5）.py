n, m = map(int, input().split())
nList = sorted(list(map(int, input().split())))

# 이미 사용한 숫자는 사용하지 않는 게 중요
# 사용 여부를 저장하는 visited 리스트를 사용하여 숫자 관리
l = []
visited = [False] * n

def dfs():
    if len(l) == m:
        print(" ".join(map(str, l)))
    else:
        for i in range(n):
            # 사용하지 않는 숫자라면 l에 추가 후 visited에 표시
            if not visited[i]:
                l.append(nList[i])
                visited[i] = True
                dfs()
                visited[i] = False
                l.pop()

dfs()