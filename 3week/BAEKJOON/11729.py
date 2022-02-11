'''

< 하노이 탑 >
https://www.acmicpc.net/problem/11729

'''

def hanoi(n, frm, to, ot):
    if n == 1:
        print(frm, to)
        return

    hanoi(n-1, frm, ot, to)
    print(frm, to)
    hanoi(n-1, ot, to, frm)

n = int(input())
print((2**n))