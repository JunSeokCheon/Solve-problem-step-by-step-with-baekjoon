def solution(s):
    zero_count = 0
    trans_count = 0
    while True:
        if s == "1":
            break
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = len(s)
        s = str(bin(s))
        s = s[2:]
        trans_count += 1
    
    return [trans_count, zero_count]