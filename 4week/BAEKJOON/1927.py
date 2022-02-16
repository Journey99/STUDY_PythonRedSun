'''

< 최소 힙 >
https://www.acmicpc.net/problem/1927

'''

# n = int(input())
# ls = []
#
# for i in range(n):
#     num = int(input())
#
#     if num > 0:
#         ls.append(num)
#     elif num == 0:
#         if len(ls) == 0:
#             print(0)
#         else:
#              ls.sort()
#              r = ls.pop(0)
#              print(r)

import heapq
import sys

input = sys.stdin.readline
n = int(input())
ls = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not ls:
            print(0)
        else:
            print(heapq.heappop(ls))
    else:
        heapq.heappush(ls, x)

