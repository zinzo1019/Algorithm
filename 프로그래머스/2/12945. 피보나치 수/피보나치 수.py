def solution(n):
    fibo_list = [0, 1]
    return fibo(fibo_list, n) % 1234567

def fibo(fibo_list, index):
    while len(fibo_list) <= index:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return int(fibo_list[index])

