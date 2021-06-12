
def closestNumbers(arr):
    arr = sorted(arr)
    pairs = []
    mini_diff = max(arr) - min(arr)
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < mini_diff:
            mini_diff = diff
            pairs = [ arr[i-1], arr[i] ]
        elif diff == mini_diff:
            pairs.extend( [ arr[i-1], arr[i] ])
    return pairs
