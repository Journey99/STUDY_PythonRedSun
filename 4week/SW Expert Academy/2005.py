'''

< 파스칼의 삼각형 >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

'''

T = int(input())

for t in range(T):
    N = int(input())

    pascal = [[1] * i for i in range(1, N+1)]      # 1로 다 채워둠

    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:     # 행의 첫번째와 마지막 원소는 그대로 1
                pass
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print(f'#{t+1}')
    for line in pascal:
        print(' '.join(map(str,line)))


