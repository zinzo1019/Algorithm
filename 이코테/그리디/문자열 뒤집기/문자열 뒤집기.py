'''
0001100
'''

list = list(map(int, input()))

count0 = 0 # 연속된 0의 총 개수 ex) 0001100 -> 2
count1 = 0 # 연속된 1의 총 개수 ex) 0001100 -> 1

# 주어진 인덱스의 값이 0이면 count0을 증가시키고,
# 1이면 count1을 증가시킨다.
def incrementGroupCount(index):
    global count0, count1
    if list[index] == 0: count0 += 1
    if list[index] == 1: count1 += 1

# 첫 번째 인덱스로 그룹 초기화
incrementGroupCount(0)
for i in range(1, len(list)):
    if list[i-1] == list[i]: continue
    else: incrementGroupCount(i)

print(min(count0, count1))