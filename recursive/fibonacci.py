# n번째 피보나치 수를 리턴
def fib(n):
    # base case
    # 1번째와 2번째 피보나치는 1이다
    if n < 3:
        return 1
    # recursive case
    # n번째 피보나치는 n - 1번째와 n - 2번째 피보나치의 합이다
    return fib(n - 1) + fib(n - 2)


for i in range(1, 11):
    print(fib(i))
