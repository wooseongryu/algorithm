# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list: list[int], index1: int, index2: int) -> list[int]:
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list: list[int], start: int, end: int) -> int:
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


# 퀵 정렬
def quicksort(my_list: list[int], start: int, end: int):
    # base case
    # 리스트의 크기는 고정이고 start와 end의 값이 바뀐다
    if end - start < 1:
        return

    pivot = partition(my_list, start, end)

    # pivot을 기준으로 다시 quicksort를 한다
    # 사용 하는 리스트는 고정이고 정렬을 할 범위를 달리한다
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)


# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
