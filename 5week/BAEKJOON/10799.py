'''

< 쇠 막대기 >
https://www.acmicpc.net/problem/10799


'''


pip_laser = input().strip()       # 양옆 공백제거
stack = []
cnt = 0

for i in range(len(pip_laser)):

    if pip_laser[i] == '(':               # 열린괄호이면
        stack.append(pip_laser[i])        # 스택에 추가

    else:                                 # 닫힌괄호이면
        stack.pop()                       # 스택에서 원소하나 pop하고

        if pip_laser[i-1] == '(':         # 만약 직전괄호가 열린괄호이면 -> 레이저이므로
            cnt += len(stack)             # 스택에 남은 괄호의 개수만큼 플러스
        else:                             # 그렇지않으면 1 플러스
            cnt += 1


print(cnt)

