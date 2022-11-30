# tabluation을 이용한 피보나치를 구하는 함수
def fib_tab(n):
    fib_table = [0, 1, 1]

    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 2] + fib_table[i - 1])

    return fib_table[n]
# 시간 복잡도는 O(n), 공간 복잡도는 O(n)


# 테스트 코드
print(fib_tab(10))
print(fib_tab(1))
print(fib_tab(2))
print(fib_tab(3))
print(fib_tab(56))
print(fib_tab(132))
