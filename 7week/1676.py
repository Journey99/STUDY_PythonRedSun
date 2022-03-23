'''

백준 - 팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676

'''
import math

n = int(input())

# 팩토리얼 구하는 방법 1
# result = 1
# for i in range(1, n+1):
#     result *= i

# 팩토리얼 구하는 방법 2
# def fac(n):
#     if n > 1:
#         return n * fac(n-1)
#     else:
#         return 1
#
# result = fac(n)


# 팩토리얼 구하는 방법 3
result = math.factorial(n)
cnt = 0

while n % 10 == 0:
    n = n // 10
    cnt += 1

print(cnt)
