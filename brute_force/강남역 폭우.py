def trapping_rain(buildings: list[int]) -> int:
    # 빗물의 총량
    volume = 0
    # 첫번쨰와 마지막은 물이 찰수가 없으므로 빼고 본다
    for i in range(1, len(buildings) - 1):
        # 현재의 위치를 기준으로 좌,우의 최대값을 구한다
        left_hi = max(buildings[:i])
        right_hi = max(buildings[i + 1:])
        # 좌,우의 최대값 중 낮은 높이가 현재의 높이보다 높다면
        if min(left_hi, right_hi) > buildings[i]:
            # 그 높이에서 현재의 높이를 뺀 만큼이 물이 차는 양이 된다
            volume += min(left_hi, right_hi) - buildings[i]
    return volume
# 시간 복잡도는 O(n^2)

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
