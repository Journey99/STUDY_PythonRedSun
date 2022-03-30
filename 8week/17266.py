'''

백준 - 어두운 굴다리
https://www.acmicpc.net/problem/17266

'''

# 풀이(1)
# 단순하게 생각해서 가로등 사이사이의 값과 양 끝까지의 값 중 가장 큰 값을 선택
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))


max_size = 0
for i in range(1, m):
    # 가로등 사이의 최댓값을 구한다
    max_size = max(max_size, x[i] - x[i-1])

# 가로등 사이의 값 / 첫 기둥과 시작점까지 거리 / 마지막 기둥과 도착점까지 거리 /
max_size = max((max_size+1)//2, x[0], n-x[-1])
print(max_size)




# 풀이(2) - 이진 탐색

import math

# 굴다리의 길이
N = int(input())

# 가로등의 개수
M = int(input())

# 가로등의 위치
arr = list(map(int, input().split()))

target = []

for i, j in zip(arr[0:], arr[1:]):
    target.append(math.ceil(abs(i - j) / 2))


target.insert(0, arr[0])
target.append(N - arr[-1])


def binary_search_tree(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == target:
            return mid
        elif mid > target:
            end = mid - 1
        elif mid < target:
            start = mid + 1


print(binary_search_tree(max(target), 0, N))
