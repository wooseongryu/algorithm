def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case
    # 원판이 없을 때는 그대로 리턴한다
    if num_disks == 0:
        return
    '''
    원판이 하나일 때는 바로 end_peg로 옮기면 되고
    원판이 두개일 때는 작은 원판을 other_peg에 두고 큰 원판을 end_peg로 그리고 작은 원판을 end_peg로 옮기면 된다
    원판이 세개일 때는 나머지 작은 원판 2개를 other_peg에 두고 큰 원판을 end_peg에 두고 나머지 원판 2개를 end_peg로 옮기면 되는데
    작은 원판 두개를 옮기는 과정은 원판이 두개일 경우와 동일하므로 재귀를 시키면 된다
    원판이 그 이상인 경우에도 모두 동일하다
    '''
    # 시작 기둥과 도착 기둥을 제외한 나머지 기둥
    # 기둥은 1, 2, 3번 세개가 있으므로 총 합이 6이다
    other_peg = 6 - start_peg - end_peg

    # 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
    hanoi(num_disks - 1, start_peg, other_peg)

    # 가장 큰 원판을 start_peg에서 end_peg로 이동
    move_disk(num_disks, start_peg, end_peg)

    # 나머지 원판들을 other_peg에서 end_peg로 이동
    hanoi(num_disks - 1, other_peg, end_peg)


# 테스트 코드
hanoi(3, 1, 3)
