
n = int(input())
tsn = ['3' , '6', '9']


for i in range(1, n+1):
    cnt = 0
    num = str(i)

    for j in num:
        if j in tsn:
            cnt += 1

    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')