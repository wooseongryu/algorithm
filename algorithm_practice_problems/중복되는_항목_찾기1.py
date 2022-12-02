"""
(n + 1)의 크기인 리스트에 1부터 n까지의 임의의 자연수가 들어가면
어떤 수는 반드시 한 번은 반복된다
몇 개의 수가 여러번 중복될 수 도 있다
여기서 중복되는 요소를 찾아낼 것이다
중복되는 어떠한 수 하나만 찾아내도 된다
1, 1, 2, 2가 있으면 1또는 2를 리턴하면 된다
"""


def find_same_number(some_list):
    # for i in range(len(some_list) - 1):
    #     for j in range(i + 1, len(some_list)):
    #         if some_list[i] == some_list[j]:
    #             return some_list[i]
    # # 시간 복잡도는 O(n^2)

    # sorted_list = sorted(some_list)
    # for i in range(len(sorted_list) - 1):
    #     if sorted_list[i] == sorted_list[i + 1]:
    #         return sorted_list[i]
    # # 시간 복잡도는 O(nlgn)

    numbers = {}
    for number in some_list:
        if number in numbers:
            return number
        numbers[number] = number
    # 시간 복잡도는 O(n), 공간 복잡도는 O(n)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
