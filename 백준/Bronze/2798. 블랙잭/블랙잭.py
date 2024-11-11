from itertools import combinations

num, targetSum = map(int, input().split())
numList = list(map(int, input().split()))

combiList = list(combinations(numList, 3))
result = 0

combiSumList = []
for combi in combiList:
    combiSumList.append(sum(combi))

combiSumList.sort(reverse=True)

for combiSum in combiSumList:
    if combiSum <= targetSum:
        result = combiSum
        break
        
print(result)