
def alternatingCharacters(s):
    count = 0
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
    return count
