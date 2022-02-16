'''

< 하노이 탑 >
https://www.acmicpc.net/problem/11729

'''

n = int(input())

def hanoi(n, frm, ot, to):
    if n == 1:
        print(frm, to)
    else:
        hanoi(n-1, frm, to, ot)
        print(frm, to)
        hanoi(n-1, ot, frm, to)

print(2**n - 1)
hanoi(n,1,2,3)