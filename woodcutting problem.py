def woodcollected(arr, n, m):
    wood = 0
    for i in range(n - 1, 1, -1):
        if arr[i] - m <= 0:
            break
        wood = wood + (arr[i] - m)
    return wood
def collectwood(arr, n, k):
    arr.sort()
    low = 0
    high = arr[n-1]
    while low <= high:
        mid = low + ((high - low) // 2)
        collect = woodcollected(arr, n, mid)
        if collect == k:
            return mid
        if collect > k:
            low = mid + 1
        else:
            low = mid - 1
    return -1
arr = [20,15,10,17]
n = len(arr)
b = 7
r = collectwood(arr, n, b)
print(r)
