from itertools import product

n, m = map(int, input().split())

# 1부터 n까지 리스트 생성
nList = list(range(1, n + 1))

# 중복 제거를 위한 set 생성
seen = set()

# product는 주어진 리스트의 요소를 사용해 모든 가능한 조합을 생성한다.
for combi in product(nList, repeat=m):
    if combi not in seen:
        seen.add(combi)
        print(" ".join(map(str, combi)))
