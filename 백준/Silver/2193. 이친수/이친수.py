# 0자리, 1자리, 2자리
cases = [0, 1, 1]
for i in range(3, 91):
    cases.append(cases[i - 2] + cases[i - 1])
n = int(input())
print(cases[n])