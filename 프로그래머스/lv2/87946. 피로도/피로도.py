from itertools import permutations
def solution(k, dungeons):
    answer = 0
    # 0개부터 던전 개수만큼 돈다
    for case in permutations(dungeons, len(dungeons)):
        char = k
        temp_answer = 0
        for rounds in case:
            # 갖고 있는 피로도가 필수 피로도보다 더 많으면
            if char >= rounds[0]:
                char -= rounds[1]
                # 던전을 돈다
                temp_answer += 1
                # 없으면 멈춘다
        if temp_answer > answer:
            answer = temp_answer
    return answer