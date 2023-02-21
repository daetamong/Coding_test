n = int(input())

res = [1, 1]

for i in range(2, n+1):
    res.append(res[i-1] + res[i-2] * 2)
print(res[n]%10007)