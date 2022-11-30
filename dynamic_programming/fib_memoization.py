def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # 이미 n번째 피보나치를 계산하고 저장했다면 그 값을 바로 리턴
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치를 계산하지 않았다면 계산하고 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]


# memoization을 이용한 피보나치 구하는 함수
def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))
