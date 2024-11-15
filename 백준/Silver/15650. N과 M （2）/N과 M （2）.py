from itertools import combinations

n, m = map(int, input().split())
nList = list(i for i in range(1, n+1))

combiList = list(combinations(nList, m))

for combi in combiList:
    result = '';
    for i in range(m):
        if i != m-1:
            result += str(combi[i]) + ' '
        else:
            result += str(combi[i])
    print(result)