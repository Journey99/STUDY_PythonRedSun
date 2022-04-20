'''

백준 - https://www.acmicpc.net/problem/11727


n 개수
1  1
2  3
3  5
4  11
5  21
...

'''

n = int(input())
dp = [0,1,3]
for i in range(3, 1001):
    dp.append(dp[i-2]*2 + dp[i-1])


print(dp[n] % 10007)
