
from collections import Counter

def makingAnagrams(s1, s2):
    result1 = Counter(s1) - Counter(s2)
    result2 = Counter(s2) - Counter(s1)
    result = result1 + result2
    return sum( result.values() )
