"""
특정 기간 중 수익이 가장 큰 구간을 찾아낼 것이다
[7, -3, 4, -8]이라면
첫 날에서 7달러를 벌고 둘째 날에는 3달러를 잃은 것이다
최대 수익을 내는 구간은 [7, -3, 4]로 해당 구간에서 낸 수익은 8달러이다.
"""


# 특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수
# brute force를 사용한 방법
def sublist_max(profits):
    max_profit = profits[0]

    # for i in range(len(profits)):
    #     for j in range(i, len(profits)):
    #         if max_profit < sum(profits[i:j + 1]):
    #             max_profit = sum(profits[i:j + 1])

    for i in range(len(profits)):
        total = 0
        for j in range(i, len(profits)):
            total += profits[j]
            max_profit = max(max_profit, total)

    return max_profit
# 시간 복잡도는 O(n^2)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
