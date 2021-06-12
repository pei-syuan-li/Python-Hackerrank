
def almostSorted(arr):
    arr_c = arr.copy()
    arr_sort = sorted(arr)
    n = len(arr)
    
    if arr == arr_sort:
        print('yes')
        return 
    l = r = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            l = i
            break 
    for i in range(n-1, 0, -1 ):
        if arr[i-1] > arr[i]:
            r = i
            break 
    # swap
    arr_c[l], arr_c[r] = arr_c[r], arr_c[l]
    if arr_c == arr_sort:
        print('yes')
        print('swap', l+1, r+1)
        return 
    # reverse
    tmp = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]
    if tmp == arr_sort:
        print('yes')
        print('reverse', l+1, r+1)
        return 
    print('no')   
