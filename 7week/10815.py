'''

백준 - 숫자 카드
https://www.acmicpc.net/problem/10815

'''

# 시간초과
# n = int(input())
# n_list = list(map(int, input().split()))
#
# m = int(input())
# m_list = list(map(int, input().split()))
#
# for i in m_list:
#     if i in n_list:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
import sys

def binary_search(ls,x):
    start = 0
    end = len(ls) - 1

    while start <= end:

        mid = (start + end) // 2

        if x == ls[mid]:
            return print(1, end=" ")

        elif x < ls[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return print(0, end=" ")

n = sys.stdin.readline().rstrip()
n_list = list(map(int, input().split()))
n_list.sort()

m = sys.stdin.readline().rstrip()
m_list = list(map(int, input().split()))


for i in m_list:
    binary_search(n_list, i)