'''

< flatten >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh


'''


for i in range(10):
    n = int(input())

    box_hgt = list(map(int, input().split()))

    # 평탄화
    for _ in range(n):
        h = box_hgt.index(max(box_hgt))  # 가장 높은 상자 인덱스
        l = box_hgt.index(min(box_hgt))  # 가장 낮은 상자 인덱스

        # 높은 상자에서 낮은 상자로 옮기기
        box_hgt[h] -= 1
        box_hgt[l] += 1


    highest = max(box_hgt)
    lowest = min(box_hgt)

    print(f'#{i+1} {highest-lowest}')