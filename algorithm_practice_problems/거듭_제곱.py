"""
x를 y번 곱하면 되지만 시간 복잡도가 O(n)이 된다
O(lgn)으로 만들어 보자
"""


# x^y를 리턴하는 함수
def power(x, y):
    # if y == 0:
    #     return 1
    #
    # if y % 2 == 0:
    #     return power(x, y // 2) * power(x, y // 2)
    # else:
    #     return x * power(x, y // 2) * power(x, y // 2)
    # # 시간 복잡도는 O(n)

    if y == 0:
        return 1

    tmp = power(x, y // 2)

    if y % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp
    # 시간 복잡도는 O(lgn)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
