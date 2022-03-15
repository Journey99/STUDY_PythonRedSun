# binary search 이용

def binary_search(ls, x):
    start = 0
    end = len(ls) - 1

    while start <= end:

        mid = (start + end) // 2

        if x == ls[mid]:
            return print(1)

        elif x < ls[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return print(0)



N = int(input())
n = list(map(int, input().split()))
n.sort()

M = int(input())
m = list(map(int, input().split()))

for i in m:
    binary_search(n, i)


