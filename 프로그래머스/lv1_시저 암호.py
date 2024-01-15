def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        else:
            temp_n = n
            while temp_n > 0:
                temp_n -= 1
                if ord(i) + 1 > 122:
                    i = 'a'
                elif ord(i) + 1 > 90 and ord(i) + 1 < 92:
                    i = 'A'
                else:
                    i = chr(ord(i) + 1)
            answer += i
    return answer