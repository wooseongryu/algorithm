# 최대한 작은 수의 벌금을 계산하는 함수
def min_fee(pages_to_print):
    total = 0
    for i, page in enumerate(sorted(pages_to_print)):
        total += page * (len(pages_to_print) - i)

    return total
# 시간 복잡도는 sort가 nlgn에 for문이 n이므로
# nlgn + n 즉, O(nlgn)이다


"""
지각시 1분에 1달러씩 벌금이다
프린트는 하나고 1장에 1분이 걸린다
리스트의 정수는 프린트 해야할 페이지 수 이다
[3, 2, 1]의 경우에
그냥 리스트의 순서대로 뽑는다면
첫 번째 사람은 3분
두 번째 사람은 3 + 2분
세 번째 사람은 3 + 2 + 1분
총 11분의 시간이 걸려 11달러가 벌금이다
"""
# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
