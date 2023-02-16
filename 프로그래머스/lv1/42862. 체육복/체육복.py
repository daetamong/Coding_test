def solution(n, lost, reserve):
    # 여벌을 갖고 있는 학생도 도난당 하는 경우를 제외 -> reserve_re
    reserve_re = set(reserve) - set(lost)
    # 여벌을 갖고 있는 학생도 도난당 하는 경우를 제외 -> lost_re
    lost_re = set(lost) - set(reserve)
    # 전체 학생 중에서 도난당한 학생을 제외한 경우
    answer = n - len(lost_re)
    for case in reserve_re:
        if case - 1 in lost_re:
            lost_re.remove(case-1)
            answer += 1
        elif case + 1 in lost_re:
            lost_re.remove(case+1)
            answer += 1
    return answer