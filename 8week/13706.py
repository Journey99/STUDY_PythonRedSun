'''

백준 - 제곱근
https://www.acmicpc.net/problem/13706

'''

# 풀이(1) - 라이브러리 사용
# import math
#
# n = int(input())
# print(math.isqrt(n))


# 풀이(2) - 이진탐색
def binary_search(s, e):
    while True:
        mid = (s + e) // 2

        if (mid ** 2) == n:
            return mid
        elif mid ** 2 > n:
            e = mid
        else:
            s = mid

n = int(input())
print(binary_search(1,n))