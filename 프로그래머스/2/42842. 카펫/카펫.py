def solution(brown, yellow):
    combi_list = get_combination_list(yellow)
    print(combi_list)
    for combi in combi_list:
        count_brown = ((combi[0] + 2) * 2 + (combi[1] + 2) * 2) - 4

        if brown == count_brown:
            return [combi[0]+2, combi[1]+2]

def get_combination_list(num):
    combi_list = []
    if num == 1:
        return [[1, 1]]

    for i in range(1, num+1):
        if num % i == 0:
            combi = [i, num//i]
            combi_list.append(combi)
    return combi_list[len(combi_list)//2:]