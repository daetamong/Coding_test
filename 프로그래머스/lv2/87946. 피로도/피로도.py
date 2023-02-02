# from itertools import permutations
# def solution(k, dungeons):
#     answer = 0
#     # 0개부터 던전 개수만큼 돈다
#     for case in permutations(dungeons, len(dungeons)):
#         char = k
#         temp_answer = 0
#         for rounds in case:
#             # 갖고 있는 피로도가 필수 피로도보다 더 많으면
#             if char >= rounds[0]:
#                 char -= rounds[1]
#                 # 던전을 돈다
#                 temp_answer += 1
#                 # 없으면 멈춘다
#         if temp_answer > answer:
#             answer = temp_answer
#     return answer

answer = 0
N = 0
# 던전을 돌았는지 돌지 않았는지 체크하기 위한 리스트
visited = []

def DFS(k, cnt, dungeons):
    global answer
    # 최대로 돌 수 있는 던전의 개수를 갱신하기 위한 과정
    if cnt > answer:
        answer = cnt
        
    # 던전의 개수만큼 돌아준다
    for i in range(N):
        # 만약 보유하고 있는 피로도가 필요 피로도보다 많고, 입장했던 적이 없으면
        if k >= dungeons[i][0] and not visited[i]:
            # 입장 기록을 1로 체크해준다
            visited[i] = 1
            # 그리고 다시 다음 던전에 입장한다 (소모 피로도만큼 빼주고, 입장횟수 + 1)
            DFS(k - dungeons[i][1], cnt + 1, dungeons)
            # 만약 입장할 수 없다면 (되돌아온다면)
            visited[i] = 0
            
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    DFS(k, 0, dungeons)
    return answer