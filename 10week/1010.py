'''

백준 - 다리놓기
https://www.acmicpc.net/problem/1010

'''

bridge = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    bridge[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        for k in range(i-1, j):

            bridge[i][j] += bridge[i-1][k]


t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    print(bridge[n][m])

