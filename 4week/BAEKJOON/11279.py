'''

< 최대 힙 >
https://www.acmicpc.net/problem/11279

참고
: https://www.daleseo.com/python-heapq/

'''

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
            print(heapq.heappop(ls)[1])
    else:
        heapq.heappush(ls, (-x, x))