'''

< 스토쿠 검증 >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

스토쿠 검증하는 법
1. 가로로 검사
2. 세로로 검사
3. 3x3을 검사

'''

T = int(input())

def check(arr):

    # 가로에 중복 확인
    for i in range(9):
        chk = []
        for j in range(9):
            if chk:              # 비어있지 않으면
                if arr[i][j] in chk:            # 배열의 원소가 chk안에 있으면 중복이므로
                    return 0
            chk.append(arr[i][j])


    # 세로에 중복 확인
    for i in range(9):
        chk = []
        for j in range(9):
            if chk:
                if arr[j][i] in chk:
                    return 0

            chk.append(arr[j][i])

    # 3x3 확인
    for i in range(0, 9, 3):
        for j in range(0,9,3):
            chk = []

            for k in range(3):
                for l in range(3):
                    if chk:
                        if arr[i+k][j+l] in chk:
                            return 0

                    chk.append(arr[i+k][j+l])

    return 1




for t in range(T):
    a = [list(map(int, input().split())) for _ in range(9)]
    num = check(a)
    print(f'#{t+1} {num}')