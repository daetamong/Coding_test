n = int(input())
arr = list(map(int, input().split()))
check = [1] * n

for i in range(1, len(arr)):
    for j in range(0, i):
        # i번째 숫자가 j번째 숫자보다 크다면
        if arr[i] > arr[j]:
            check[i] = max(check[i], check[j] + 1)
        # 작거나 같다면 그냥 넘어간다
        else:
            continue
print(max(check))