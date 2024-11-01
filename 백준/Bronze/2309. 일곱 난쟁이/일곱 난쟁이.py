# 9개의 숫자 중에서 7개의 숫자의 합이 100인 경우를 출력하라.

import math
from itertools import combinations, permutations

numberList = [int(input()) for _ in range(9)]
numberList.sort()

totalNumberList = sum(numberList)
overNum = totalNumberList - 100

combinations = list(combinations(numberList, 2))
for combi in combinations:
    if sum(combi) == overNum:
        resultArr = [x for x in numberList if x not in combi]
        print(*resultArr, sep='\n')
        break