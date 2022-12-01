# 한 사람의 카드 뭉치당 카드를 하나씩 뽑아서 모두 곱했을 때 가능한 최대 곱을 리턴
def max_product(card_lists):
    total_max = 1

    for card_list in card_lists:
        # 하나의 카드 뭉치에서 최대값을 계속 곱한다
        total_max *= max(card_list)

    return total_max


# 테스트 코드
# 첫 번째 플레이어는 카드 1, 6, 5를 가지고 있고
# 두 번째 플레이어는 카드 4, 2, 3을 가지고 있다
# 첫 번째 플레이어의 6과 두 번째 플레이어의 4를 곱한 것이 최대값이다
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
