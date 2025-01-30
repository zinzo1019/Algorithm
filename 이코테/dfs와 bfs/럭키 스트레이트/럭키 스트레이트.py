'''
123402
'''

arr = list(map(int, input()))
countLeft = 0
countRight = 0

for i in range(len(arr)):
    if i < len(arr) / 2:
        countLeft += arr[i]
    else:
        countRight += arr[i]

result = "LUCKY" if (countLeft == countRight) else "READY"
print(result)