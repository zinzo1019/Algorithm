# N, M, K = 5, 8, 3
# nList = [2, 4, 5, 4, 6]

N, M, K = map(int, input().split())
nList = list(map(int, input().split()))
result = 0

nList.sort(reverse=True)

k = 0
for m in range(M):
    if k == 3:
        result += nList[1]
        k = 0
    else:
        result += nList[0]
        k += 1

print(result)