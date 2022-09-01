def allocationpossible(a, n, m,k):
    pages = 0
    std = 1
    for i in range(0,n):
        if a[i]>m :
            break
        if a[i]+pages>m:
            std+=1
            pages+=a[i]
            if std > k:
                break
    pages+=a[i]

def minipage(a, n, b):
    a.sort()
    low = a[0]
    high = sum(a)
    while low<=high:
        mid = low+(high-low)//2
        allocate = allocationpossible(a,n,mid,k)
        if allocate == b:
            return mid
        if allocate > b:
            high = mid-1
        else:
            low= mid +1
    return -1

a = [12,34,67,90]
n = len(a)
k = 2
print(minipage(a,n,))


