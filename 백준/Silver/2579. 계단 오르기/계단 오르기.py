n = int(input())
step = []
for i in range(n):
    step.append(int(input()))

# 각 계단별로 최대값을 구하기 위한 딕셔너리
step_dic = {idx : 0 for idx, val in enumerate(step)}
#print('step : ', step)
#print('step_dic : ', step_dic)
#print('\n')

if len(step_dic) <= 2:
    print(sum(step))
else:
    step_dic[0] = step[0]
    step_dic[1] = step[0] + step[1]
    #print('step 1 : ', step_dic)
    step_dic[2] = max(step[1] + step[2], step[0] + step[2])
    #print('step 2 : ', step_dic)
    
    for i in range(3, len(step)):
        step_dic[i] = max(step_dic[i-3] + step[i-1] + step[i], step_dic[i-2] + step[i])
        #print('{} step : '.format(i), step_dic)

    print(step_dic.get(n-1))