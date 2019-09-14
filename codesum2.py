def codesum2(s):
    total=0
    for i in range (len(s)):
        total=total+ord(s[i])
    return total
