n = int(input())
color_list = []

# 각 집마다 색깔을 칠했을 때 발생하는 비용을 담은 리스트
for i in range(n):
    color_list.append(list(map(int, input().split())))
   
# 1층은 고정이므로 index = 1부터 시작
for i in range(1, len(color_list)):
    # i층의 0번째 집 = (전 층의 1번째 집과 2번째 집의 최소값) + i층의 0번째 집 색깔 비용
    color_list[i][0] = min(color_list[i-1][1], color_list[i-1][2]) + color_list[i][0]
    color_list[i][1] = min(color_list[i-1][0], color_list[i-1][2]) + color_list[i][1]
    color_list[i][2] = min(color_list[i-1][0], color_list[i-1][1]) + color_list[i][2]
# 마지막 층에서 비용의 합계가 계산 = 최소값
print(min(color_list[n-1][0], color_list[n-1][1], color_list[n-1][2]))