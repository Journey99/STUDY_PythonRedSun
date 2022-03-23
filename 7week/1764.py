'''

백준 - 듣보잡
https://www.acmicpc.net/problem/1764

'''
import sys

n, m = map(int, input().split())

hear = [sys.stdin.readline().rstrip() for i in range(n)]
see = [sys.stdin.readline().rstrip() for i in range(m)]

hear_see = list(set(hear) & set(see))
hear_see.sort()

print(len(hear_see))
for i in hear_see:
    print(i)
