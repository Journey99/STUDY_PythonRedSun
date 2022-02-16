'''


< 스택 수열 >
https://www.acmicpc.net/problem/1874

'''

n = int(input())
sequence = [int(input()) for _ in range(n)]
current = 1
stack = []
answer = []

for i in sequence:
    while current <= i:
        stack.append(current)
        answer.append('+')
        current += 1

    if stack[-1] == i:
        answer.append('-')
        stack.pop()

if not stack:
    print('\n'.join(answer))
else:
    print("No")
    