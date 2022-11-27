# 두가지 카드 뭉치에서 하나씩 뽑은 두 수의 곱이 가장 큰 값을 리턴하는 함수
def max_product(left_cards, right_cards):
    # 각 리스트의 첫 번째 요소의 곱을 최대값으로 설정하고 시작
    max_value = left_cards[0] * right_cards[0]
    for i in left_cards:
        for j in right_cards:
            # 현재까지의 최대값과 현재의 i*j값을 비교해 큰 값을 max_value에 저장
            max_value = max(max_value, i * j)

    # 마지막까지 저장되어 있는 값이 최대값
    return max_value
# 시간 복잡도는 O(n^2)

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))