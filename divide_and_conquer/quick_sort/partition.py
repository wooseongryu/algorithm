# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list: list[int], index1: int, index2: int) -> list[int]:
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list: list[int], start: int, end: int) -> int:
    """
    리스트를 네 그룹으로 나누어 생각한다
    먼저 리스트의 가장 마지막 요소를 pivot으로 잡고
    pivot보다 작은 것을 small, 큰 것을 big, 아직 비교되지 않은 것을 unknown이라 한다
    리스트의 마지막 즉 pivot의 인덱스를 변수 p에 담는다
    전체 리스트의 시작 인덱스는 start, big의 시작 인덱스는 b, unknown의 시작 인덱스는 i이다
    가장 처음에 시작될 때는 start, b, i 모두 0번 인덱스에서 시작한다
    p번 인덱스와 i번 인덱스를 비교해서 p보다 크다면 i++을 한다
    p보다 작다면 p번 인덱스와 i번 인덱스의 위치를 바꾸고 b++, i++을 한다
    i == p가 되어 모두 비교를 하게 되면 p와 b의 위치를 바꾼다
    만약 리스트 [4, 3, 6, 2, 7, 1, 5]가 있다면
    5가 pivot이 되고 먼저 4와 비교한다
    pivot보다 작으니 big그룹의 가장 첫번째 인덱스와 위치를 교환한다
    그러면 big그룹을 한칸 뒤로 밀게된 셈이 되고 그 자리에 small그룹의 값을 넣는다
    그리고 big그룹이 한칸 밀렸으니 b를 하나 증가시켜 big그룹의 시작 인덱스를 옮겨준다
    big그룹을 밀고 생긴 공간이 small그룹의 공간이 된다
    이렇게 되면 small그룹은 항상 천체 리스트의 가장 앞부분에 오게되니
    start가 곧 small그룹의 가장 첫번째 인덱스가 되고 b이전 까지가 small그룹의 마지막 범위다
    pivot과 6을 비교하면 6이 더 크니 i만 하나 증가시며 unknown그룹을 줄여나간다
    그리고 pivot보다 클 때나 작을 때나 i를 증가시켜 unknown범위를 줄여나간다
    비교가 모두 끝나면 big그룹의 시작 인덱스와 pivot을 교환한다
    전체적인 그림을 보면 pivot보다 크면 그자리에 두고 작으면 전체 리스트의 가장 앞부분 부터
    big그룹을 뒤로 밀어가며 small그룹의 자리를 만들어 채운다
    unknown그룹이 없어지면, 즉 리스트의 모든 요소를 pivot과 비교하고 나면
    big그룹을 한칸 뒤로 밀고 그자리에 pivot을 넣어 pivot을 기준으로 small, big그룹을 나누게 된다
    """
    b = start
    i = start
    p = end

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)

    return b


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
