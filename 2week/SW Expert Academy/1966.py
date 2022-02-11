'''

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq

'''

t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()

    print(f"#{i+1}", end=" ")

    for j in range(n):
        print(num[j], end=" ")

    print()
