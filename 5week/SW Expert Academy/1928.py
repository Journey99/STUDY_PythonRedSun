'''

< base64 decoder >
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq

'''

import base64

T = int(input())
for t in range(T):
    s = input()
    # s_encode = s.encode("UTF-8")
    se_decode = base64.b64decode(s)

    print(f'#{t+1} {se_decode.decode("UTF-8")}')




# from base64 import b64decode
#
# T = int(input())
# for t in range(1, T+1):
#     print(f'#{t} {b64decode(input()).decode("UTF-8")}')