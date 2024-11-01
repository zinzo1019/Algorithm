from itertools import product

# T 개
number = int(input())

# T 개의 자연수
numberList = []
for i in range(0, number):
    numberList.append(int(input()))

eurekaList = []
for i in range(1, 50):
    result = int(i * (i + 1) / 2)
    eurekaList.append(result)

combinations = list(product(eurekaList, eurekaList, eurekaList))

def determineEureka(num):
    for combi in combinations:
        if sum(combi) == num:
            return True
    return False

for num in numberList:
    if determineEureka(num):
        print(1)
    else:
        print(0)
