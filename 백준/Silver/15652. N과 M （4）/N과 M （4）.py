n, m = map(int, input().split())

# l에는 한 조합을 순차적으로 담는다. 예: [1] -> [1, 1] -> [1, 1, 1]
# l의 크기가 m과 같아진다면 출력하고 함수를 끝낸다. 예: m의 크기 3 == [1, 1, 1]의 크기 3 -> print
# l의 크기와 m과 다르면 dfs() 함수를 재호출한다.
# 한 조합을 출력하면 리스트 l을 다시 비우고 (l.pop()) 다음 for문을 실행한다.
l = []
def dfs(startNum):
    if len(l) == m:
        print(" ".join(map(str, l)))
    else:
        for i in range(startNum, n+1):
            l.append(i)
            dfs(i)
            l.pop()

dfs(1)