
import math
def encryption(s):
    s = s.replace(' ', '')
    n = len(s)
    #r = math.floor( math.sqrt(n) )
    c = math.ceil( math.sqrt(n) )
    result = []
    for j in range(c):
        temp = []
        i = 0
        while i+j <n :
            temp.append( s[j+i] )
            i+=c
        result.append( "".join(temp) )
        print( temp, result )
    return ' '.join(result)
