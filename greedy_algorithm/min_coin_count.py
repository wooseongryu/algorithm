# 최소 개수의 동전으로 돈을 거슬러 주는 함수
def min_coin_count(value, coin_list):
    count = 0

    for coin in sorted(coin_list, reverse=True):
        # 현재의 동전으로 몇 개를 거슬러 줄 수 있는지
        count += value // coin

        # 잔액 계산
        value %= coin

    return count


# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
