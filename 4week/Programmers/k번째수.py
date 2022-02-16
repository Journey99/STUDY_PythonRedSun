def solution(array, commnads):
    answer = []

    for commnad in commnads:
        ls = array[commnad[0]-1 : commnad[1]]
        ls.sort()
        answer.append(ls[commnad[2]-1])

    return answer