'''

< 괄호 >

https://www.acmicpc.net/problem/9012

'''


# n = int(input())
#
# for _ in range(n):
#
#     a = list(input())
#     sum = 0
#
#     for i in a:
#         if i == '(':
#             sum += 1
#
#         elif i == ')':
#             sum -= 1
#
#         if sum < 0:
#             print("NO")
#             break
#
#     if sum > 0:
#         print('NO')
#
#     elif sum == 0:
#         print('YES')
#

n = int(input())

for i in range(n):
    stack = []
    a = input()

    for j in a:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:  # 괄호가 있으면
                stack.pop()
            else:  # 괄호가 없으면
                print("NO")
                break
        else:
            print("NO")
            break

    if len(stack) != 0:
        print("NO")
    else:
        print("YES")
