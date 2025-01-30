'''
02984
'''

list = list(map(int, input()))

result = 1
for l in list:
    if l <= 1:
        result += l
    else:
        result *= l

print(result)