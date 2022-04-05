'''

백준 - 기타 레슨
https://www.acmicpc.net/problem/2343

'''

n, m = map(int, input().split())
minute = list(map(int,input().split())) # [int(input()) for _ in range(n)]

left = max(minute)
right = sum(minute)

while left <= right:
    mid = (left + right) // 2
    min_sum = 0
    cnt = 1          # 블루레이 개수

    for x in minute:
        min_sum += x
        if min_sum > mid:
            cnt += 1
            min_sum = x

    if cnt > m:
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)
