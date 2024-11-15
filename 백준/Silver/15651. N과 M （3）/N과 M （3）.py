from itertools import product

n, m = map(int, input().split())

# Generate a sorted list from 1 to n
nList = list(range(1, n + 1))

# Use a set to track seen combinations and print unique results directly
seen = set()

for combi in product(nList, repeat=m):
    if combi not in seen:
        seen.add(combi)
        print(" ".join(map(str, combi)))
