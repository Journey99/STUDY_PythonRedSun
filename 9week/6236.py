'''

백준 - 용돈관리
https://www.acmicpc.net/problem/6236

'''

n, m = map(int, input().split())
money_list = [int(input()) for _ in range(n)]
left = min(money_list)
right = sum(money_list)
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1                           # 인출 횟수
    tmp = mid                         # 현재 가진 돈

    for money in money_list:
        if tmp < money:             # 돈이 부족하면 인출하고 횟수 증가
            tmp = mid
            cnt += 1

        tmp -= money

    # m번보다 더 많이 인출하거나 인출한 금액이 하루를 다 살기에 적은 경우
    if cnt > m or mid < max(money_list):
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result)





