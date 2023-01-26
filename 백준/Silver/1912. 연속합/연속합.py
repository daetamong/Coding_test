n = int(input())
l = list(map(int, input().split()))
check = [0] * len(l)
check[0] = l[0]

for i in range(1, len(l)):
    check[i] = max(check[i-1] + l[i], l[i])
print(max(check))