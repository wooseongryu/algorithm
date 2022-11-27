# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    return triangle_number(n - 1) + n


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
