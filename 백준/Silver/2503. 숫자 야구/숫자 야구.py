from itertools import permutations

permuList = list(permutations([i for i in range(1, 10)], 3))
candiList = []

for _ in range(int(input())):
    candi = list(map(int, input().split()))
    candiList.append(candi)

result = 0
for permu in permuList:
    match = True
    for candi in candiList:
        num_str = str(candi[0])  # 정수를 문자열로 변환하여 각 자리 비교
        strike, ball = candi[1], candi[2]
        strikeNum, ballNum = 0, 0

        # permu와 num_str의 각 자리 비교
        for i in range(3):
            if str(permu[i]) == num_str[i]:  # 각 자리의 숫자가 정확히 일치하는지 확인
                strikeNum += 1
            elif str(permu[i]) in num_str:   # 다른 자리에서 숫자가 일치하는지 확인
                ballNum += 1

        # strike와 ball 조건이 맞지 않으면 현재 permu는 후보에서 제외
        if strikeNum != strike or ballNum != ball:
            match = False
            break

    # 모든 조건을 만족하면 결과에 포함
    if match:
        result += 1

print(result)
