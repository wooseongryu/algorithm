# 두 리스트를 받아서 하나의 정렬된 리스트를 리턴
def merge(list1: list[int], list2: list[int]) -> list[int]:
    merged_list = []
    i = 0
    j = 0
    
    # 두 리스트에서 작은 값을 먼저 가져와 merged_list에 추가
    # 두 리스트 중에서 한쪽이 모두 소진될 때 까지
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # 나머지 남은 쪽의 리스트의 요소들을 모두 추가
    if i == len(list1):
        merged_list += list2[j:]
    else:
        merged_list += list1[i:]

    return merged_list


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
