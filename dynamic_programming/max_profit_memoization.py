def max_profit_memo(price_list, count, cache):
    # base case
    # count가 0, 1인 경우에는 그 값을 그대로 리턴
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이미 계산한 값이면 cache에 저장된 값을 리턴
    if count in cache:
        return cache[count]

    # profit에 가능한 최대 수익을 저장한다
    # 팔려고 하는 총 개수에 대한 가격이 price_list에 있으면 그 값을 저장하고
    # 없으면 0으로 저장
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해 최대값을 뽑아낸다
    # 5개를 팔때는 5, 4+1, 3+2의 경우가 있다
    # 카운트만큼 다 돌리면 4+1, 3+2, 2+3, 1+4이렇게 중복되니 반으로 줄인다
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    cache[count] = profit

    return profit


# 가능한 최대 수익을 리턴 시키는 함수
def max_profit(price_list, count):
    """
    5개를 팔아서 가능한 최대 수익을 찾으려면 4개를 팔아서 가능한 최대수익, 3개를...
    이렇게 알아야 한다. 즉, 부분 문제들을 풀어야 한다
    """
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트 코드
# 1개에 100원, 2개에 400원, 3개에 800원, 4개에 900원, 5개에 1000원
# 5개를 팔아서 최대한의 이익을 낼 수 있는 방법은?
# 3개, 2개를 팔아 1200원이 최대 수익
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
