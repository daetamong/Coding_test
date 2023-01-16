from collections import Counter
def solution(topping):
    answer = 0
    # 토핑의 종류와 개수를 파악하기 위한 딕셔너리 : 언니가 먹을 토핑 종류
    first = Counter(topping)
    # 동생이 먹을 토핑 종류
    second = set()
    for case in topping:
        # 동생에게 넘겨줄 토핑
        first[case] -= 1
        # 동생이 받은 토핑
        second.add(case)
        # 동생에게 넘겨주고 토핑이 없으면
        if first[case] == 0:
            # 언니가 먹을 토핑 리스트에서 제거
            first.pop(case)
        # 그러고 나서 동생이 먹을 토핑 개수와 언니가 먹을 토핑 개수가 같으면 정답에 +1
        if len(first) == len(second):
            answer += 1
    return answer