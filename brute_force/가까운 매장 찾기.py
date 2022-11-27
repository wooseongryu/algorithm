# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1: tuple[int, int], store2: tuple[int, int]) -> float:
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # 현재 까지의 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]
    
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            tmp1, tmp2 = coordinates[i], coordinates[j]
            # 현재 까지의 가장 가까운 값보다 현재의 값이 더 가깝다면
            if distance(pair[0], pair[1]) > distance(tmp1, tmp2):
                pair = [tmp1, tmp2]

    return pair
# 시간 복잡도는 O(n^2)

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
