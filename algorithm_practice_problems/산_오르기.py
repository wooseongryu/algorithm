"""
1km당 1L의 물을 마셔야 한다
약수터를 최대한 적게 들리고 등산할 것이다
select_stops함수는 약수터 위치 리스트와 물통의 용량을 받는다
시작시의 물통은 가득 채워진 상태이고 약수터에서는 항상 물을 가득 채운다
마지막 약수터를 들리면 성공적으로 등산한 것이다
물통의 용량이 4고 약수터 위치가 [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]라면
[4, 7, 11, 13, 16, 20, 24, 26]가 결과값이다
26km까지 가능 방법은 24km까지 가능 방법 + 26km 약수터와
22km까지 가능 방법 + 26km 약수터이다 그러므로 최적 부분 구조가 있다
항상 가능한 먼 약수터로 가는 것이 가장 좋은 선택이므로 탐욕적 선택 속성이 있다
"""


def select_stops(water_stops, capacity):
    # 약수터 리스트
    point = []

    # 마지막으로 들린 약수터
    last_stop = 0

    for i in range(len(water_stops) - 1):
        # 현재의 약수터를 기준으로 마지막으로 들렀던 약수터에서
        # 그다음 약수터 까지 한번에 갈 수 없다면 현재 위치에서 채운다
        if capacity < water_stops[i + 1] - last_stop:
            point.append(water_stops[i])
            last_stop = water_stops[i]

    # 마지막 약수터는 무조건 포함되어야 한다
    point.append(water_stops[-1])

    return point


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
