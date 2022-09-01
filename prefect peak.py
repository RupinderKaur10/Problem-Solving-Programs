def findPeakUtil(arr, low, high, n):
    mid = low + (high - low) / 2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] >= arr[mid])):
        return 1
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    elif (mid > 0 and arr[mid + 1] < arr[mid]):
        return findPeakUtil(arr, (mid + 1), high, n)
    else:
        return 0
def findPeak(arr, n):
    return findPeakUtil(arr, 0, n - 1, n)


# arr = []
# n = int(input("enter the number of elements:\n"))
# for i in range(0, n):
#     e = int(input("enter the element ["+str(i)+"] in list:\n"))
#     arr.append(e)
# print(arr)
arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
n = len(arr)
print(findPeak(arr, n))
