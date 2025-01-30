'''
5
2 3 1 2 2
'''

n = int(input())
list = list(map(int, input().split()))

# 오름차순
list.sort(reverse=False)

num = 1
result = 0

for l in list:
    # 그룹 완성
    if num == l:
        result += 1
        # 그룹 초기화
        num = 1

    # 그룹 완성 X
    # 그룹에 한 명 추가
    else:
        num += 1

print(result)