'''
3 3
3 1 2
4 1 4
2 2 2
'''
'''
2 4
7 3 1 8
3 3 3 4
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

minArr = [min(a) for a in arr]
print(max(minArr))