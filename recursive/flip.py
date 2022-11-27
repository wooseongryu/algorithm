# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    # 리스트 길이가 1이면 뒤집을게 없으므로 그대로 리턴
    if len(some_list) < 2:
        return some_list
    # recursive case
    return some_list[-1:] + flip(some_list[:-1])


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
