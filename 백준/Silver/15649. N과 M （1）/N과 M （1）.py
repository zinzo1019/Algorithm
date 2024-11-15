from itertools import permutations

n, m = map(int, input().split())
nList = list(i for i in range(1, n+1))

permuList = list(permutations(nList, m))

for permu in permuList:
    result = '';
    for i in range(m):
        if i != m-1:
            result += str(permu[i]) + ' '
        else:
            result += str(permu[i])
    print(result)