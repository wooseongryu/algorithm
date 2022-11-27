# n부터 m까지의 합을 리턴한다
def consecutive_sum(start: int, end: int) -> int:
    # base case
    if start == end:
        return start

    middle = (start + end) // 2

    return consecutive_sum(start, middle) + consecutive_sum(middle + 1, end)


# 테스트
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 8))
