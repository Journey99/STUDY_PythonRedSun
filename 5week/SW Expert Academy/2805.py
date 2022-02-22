'''

< 농작물 수확하기 >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB

'''

T = int(input())

for t in range(1, T+1):
    n = int(input())

    farm = [list(map(int, input().split())) for _ in range(n)]
    mid = n // 2
    l = mid
    r = mid
    sum = 0

    for i in range(n):
        for j in range(l, r+1):
            sum += farm[i][j]

        if i <= mid:
            l -= 1
            r += 1

        else:
            l += 1
            r -= 1

    print(sum)

