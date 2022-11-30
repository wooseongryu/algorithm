# tabulation에서 테이블을 모두 채우지 않고 공간 효율성을 개선시킨 함수
def fib_optimized(n):
    front = 0
    back = 1

    # n이 1이면 반복문을 돌 필요가 없다 back을 그대로 리턴
    for i in range(1, n):
        front, back = back, front + back

    return back
# 테이블을 모두 채우지 않고 공간을 최적화한 방식
# 공간 복잡도는 O(1)이다.


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
