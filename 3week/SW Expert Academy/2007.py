'''

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq

'''


T = int(input())

for i in range(1,T+1):
    pattern = input()
    start = pattern[0]

    for j in range(1, len(pattern)):
        if pattern[j] == start and pattern[0:j] == pattern[j:j*2]:
            index = j
            break

    print(f'#{i} {index}')