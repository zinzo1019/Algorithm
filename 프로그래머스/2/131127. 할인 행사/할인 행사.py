def solution(want, number, discount):
    answer = 0

    want_product_count_map = {}
    for i in range(len(want)):
        want_product_count_map[want[i]] = number[i]

    product_count_map = {}
    for i in range(10):
        try:
            product_count_map[discount[i]] += 1
        except:
            product_count_map[discount[i]] = 1
    if is_valid(want_product_count_map, product_count_map):
        answer += 1

    index = 10
    while index < len(discount):
        # 날짜가 지난 상품 제거
        product_count_map[discount[index - 10]] -= 1
        try:
            product_count_map[discount[index]] += 1
        except:
            product_count_map[discount[index]] = 1
        index += 1

        if is_valid(want_product_count_map, product_count_map):
            answer += 1

    return answer

def is_valid(map1, map2):
    for key, val in map1.items():
        try:
            if map2[key] != val:
                return False
        except:
            return False
    return True