'''
< 그룹 단어 체커 >

https://www.acmicpc.net/problem/1316

'''

n = int(input())
cnt = 0

for i in range(n):
    word = input()
    for idx, w in enumerate(word):

        # print(idx,w)

        if idx != len(word)-1:
            if w != word[idx+1]:
                if w in word[idx+1:]:
                    break
        else:
            cnt += 1
print(cnt)