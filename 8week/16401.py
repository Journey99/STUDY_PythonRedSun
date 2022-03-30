'''

백준 - 과자 나눠주기
https://www.acmicpc.net/problem/16401

'''

# # m : 조카의 수 , n : 과자의 수
# m, n = map(int, input().split())
# # 과자 길이
# length = list(map(int, input().split()))
#
# start = 0
# end = max(length)
#
# ggagga = 0
#
# # 이분탐색 시작
# while start <= end:
#     mid = (start + end) // 2
#
#     # mid개로 나눠줄 수 있는 인원이 m명보다 크거나 같으면
#     if sum([i // mid for i in length]) >= m:
#         ggagga = mid
#         start = mid + 1
#
#     else:
#         end = mid - 1
#
# print(ggagga)

# 런타임 에러


# 다른사람 풀이
import sys


m, n = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))

left = 1  # 최소 크기
right = max(snack) # 최대 크기
answer = 0  # 다 나눠줄 수 없는 경우

while left <= right :  # 이분탐색 기저조건
    mid = int((left + right)/2)
    count = 0
    for s in snack:
        if s < mid:
            continue
        else:
            count += int(s/mid)
    if count >= m:  # 다 나눠줄 수 있는 경우 더 큰 수 탐색
        answer = mid
        left = mid + 1
    else:
        right = mid-1
print(answer)





