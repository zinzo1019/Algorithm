arr = list(map(int, input()))

half = len(arr) // 2
countLeft = sum(arr[:half])
countRight = sum(arr[half:])

result = "LUCKY" if (countLeft == countRight) else "READY"
print(result)