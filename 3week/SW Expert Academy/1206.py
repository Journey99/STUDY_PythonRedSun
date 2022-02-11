'''

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

'''


for t in range(1,11):
    n = int(input())
    building = list(map(int, input().split()))

    view = 0
    for i in range(2, n-2):
        high1 = building[i] - building[i-2]
        high2 = building[i] - building[i-1]
        high3 = building[i] - building[i+1]
        high4 = building[i] - building[i+2]

        if high1 > 0 and high2 > 0 and high3 > 0 and high4>0:
            view = min(high1, high2, high3, high4)

    print("#{} {}".format(t, view))

