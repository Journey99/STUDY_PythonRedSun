'''

백준 - 먹을 것인가 먹힐 것인가
https://www.acmicpc.net/problem/7795

https://docs.python.org/ko/3/library/bisect.html

'''
# import sys
# import bisect
#
# input = sys.stdin.readline
#
# for _ in range(int(input())):
#
#     n, m = map(int, input().split())
#     a = sorted(list(map(int, input().split())))
#     b = sorted(list(map(int, input().split())))
#     cnt = 0
#
#     for x in a:
#         cnt += (bisect.bisect(b, x-1))
#
#     print(cnt)


# 다른 풀이

for _ in range(int(input())):

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    p = cnt = 0
    for i in range(n):
        while p < m and a[i] > b[p]:
            p += 1
        cnt += p

    print(cnt)