
def breakingRecords(scores):
    max_break = min_break = 0
    max_s = min_s = scores[0]
    for i in range( 1, len(scores) ):
        if scores[i] > max_s :
            max_break += 1
            max_s = scores[i]
        if scores[i] < min_s :
            min_break += 1
            min_s = scores[i]
    return max_break, min_break
