'''
< 단어 공부 >

문제 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
      단, 대문자와 소문자를 구분하지 않는다.

입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다

출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
      단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

https://www.acmicpc.net/problem/1157

'''


word = input().upper()

# 알파벳 개수 세기
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 가장 많이 사용된 알파벳 찾기
max_key = max(dic, key=dic.get)   # key를 기준으로 최댓값 찾기
max_value = dic[max_key]
dic.pop(max_key)
if max_value in dic.values():
    print("?")
else: print(max_key)


'''
import collections

word = input().upper()
word = list(word)
cnt = collections.Counter(word)   # 요소의 개수를 딕셔너리 형태로 반환
cnt_max = []

for i, j in cnt.items():
    if j == max(cnt.values()):
        cnt_max.append(i)
        if len(cnt_max) > 1:
            print("?")
            break

print(cnt_max[0])

'''
