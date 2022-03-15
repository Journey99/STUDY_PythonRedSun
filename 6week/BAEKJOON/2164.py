# n = int(input())
#
# ls = [i for i in range(1, n+1)]
#
# while len(ls) > 1:
#     ls.pop(0)
#     ls.append(ls.pop(0))
#
# print(ls[0])


from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

while (len(deque)) > 1:
    deque.popleft()
    move = deque.popleft()
    deque.append(move)

print(deque[0])

