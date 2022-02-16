'''

< 달팽이 숫자 >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

참고 : https://somefood.github.io/algorithm/2020/07/13/algorithm_snail/

'''

def snail(n):
    arr = [[0 for j in range(n)] for i in range(n)]    # 배열을 0으로 초기화
    row = 0
    col = -1
    cnt = 1
    trans = 1

    while n > 0:
        for _ in range(n):   # 행은 고정
            col += trans
            arr[row][col] = cnt
            cnt += 1

        n -= 1

        for _ in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1

        trans *= -1

    return arr

T = int(input())

for i in range(T):
    n = int(input())
    arr = snail(n)
    print(f'#{i+1}')
    for line in arr:
        print(' '.join(map(str,line)))