
def timeInWords(h, m):
    time = { 1: 'one', 2:'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
            8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
            14: 'fourteen', 16: 'sixteen', 17: 'eleventeen', 18: 'eighteen', 19: 'nineteen', 
            20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 
            24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 
            28: 'twenty eight', 29: 'twenty nine' }
    answer = ''
    if m ==0:
        answer = time[h] + " o' clock"
    elif m==30 :
        answer = 'half past ' + time[h]
    elif m <30:
        if m ==1 :
            answer = time[m] + ' minute past ' + time[h] 
        elif m ==15:
            answer = 'quarter past ' + time[h]             
        else:
            answer = time[m] + ' minutes past ' + time[h]  
    else: # m >60
        h = 1 if h==12 else h+1
        m = 60-m
        if m ==1:
            answer = time[m] + ' minute to ' + time[h]
        elif m ==15:    
            answer = 'quarter to ' + time[h]   
        else:
            answer = time[m] + ' minutes to ' + time[h]  
    return answer
