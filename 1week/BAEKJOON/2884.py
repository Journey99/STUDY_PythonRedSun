"""
< 알람 시계 >

문제 : 맞춰진 알람을 45분 앞서는 시간으로 바꾸기!

https://www.acmicpc.net/problem/2884

"""

h, m = map(int, input().split())

if m >= 45:                  # 분이 45분 이상이면 분에서만 45를 빼주면 된다
    m -= 45
else:
    if h == 0:              # 0시일 경우 24시와 같으므로
        h = 23              # 23시로 바뀌고
        m += 15             # m + 60 에다가 다시 -45를 해야하므로 한번에 m += 15
    else:
        h -= 1
        m += 15

print(h, m)