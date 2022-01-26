"""

문제 : 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라

입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

"""

t = int(input())
for i in range(t):
    sum = 0
    arr = list(map(int, input().split()))

    for j in arr:
        if j % 2 != 0:
            sum += j

    print("#{} {}".format(i+1, sum))

# 파이서닉하게
"""
t = int(input())
for i in range(t):
    nums = map(int, input().split())
    result = sum(n for n in nums if n % 2 == 1)
    print("#{} {}".format(i+1, result)

"""