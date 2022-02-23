'''

< 농작물 수확하기 >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB

'''

T = int(input())

for t in range(1, T+1):
    n = int(input())

    farm = [list(map(int, input().split())) for _ in range(n)]   # 배열을 만들고
    mid = n // 2       # 배열의 중앙
    l = mid
    r = mid
    sum = 0

    for i in range(n):
        for j in range(l, r+1):
            sum += farm[i][j]

        if i < mid:        # 가운데를 기준으로 위쪽은 양옆을 하나씩 추가
            l -= 1
            r += 1

        else:              # 가운데를 기준으로 아래쪽은 양옆을 하나씩 제거
            l += 1
            r -= 1

    print(sum)

