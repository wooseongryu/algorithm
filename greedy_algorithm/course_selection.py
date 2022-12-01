# 최대한 많은 수업을 들을 수 있는 조합을 리턴하는 함수
def course_selection(course_list):
    # 수업이 끝나는 시간을 기준으로 정렬한다
    # 앞에 수업과 비교하며 겹치지 않는 수업만 추가할 것이다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 수업이 가장 먼저 끝나는 것은 무조건 듣는다
    my_list = [sorted_list[0]]

    # 이미 선택한 수업과 겹치지 않는 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 겹치지 않는 수업만 추가한다
        if my_list[-1][1] < course[0]:
            my_list.append(course)

    return my_list
# 시간 복잡도는 O(nlgn)

# 테스트 코드
# 각 튜플의 0번째 항목은 수업의 시작시간, 1번째 항목은 종료시간
# (2, 5)와 (4, 7)은 겹쳐서 같이 들을 수 없다
# (2, 5)와 (5, 7)같이 끝과 시작이 겹치는 수업은 들을 수 없다고 가정


print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
