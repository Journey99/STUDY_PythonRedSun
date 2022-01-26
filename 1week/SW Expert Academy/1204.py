"""
< 최빈수 구하기 >

"""

from collections import Counter
import sys

t = int(input())
for i in range(1, t+1):

    scores = list(map(int, sys.stdin.readline()))
    most_num = Counter(scores).most_common()[0][0]

    print("#{} {}".format(i, most_num))