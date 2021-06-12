
def weightedUniformStrings(s, queries):
    d = {}
    weight = 0
    result = []
    for i in range( len(s) ):
        if i ==0 or s[i] != s[i-1]:
            weight = ord(s[i]) - ord('a') +1 
        else:
            weight = weight + ord(s[i]) - ord('a') +1 
        d[weight] = 1
    for j in queries:
        if j in d:
            result.append('Yes')
        else:
            result.append('No')
    return result
