def rotate(d,arr):
    #one way
    arr = arr[d:] + arr[:d]
    return arr
    #second way
    # for value in (arr[d:] + arr[0:d]):
    #     print(value, end = " ")

    # a = [35, 56, 48, 21, 87]
    # N = len(a)
    # K = 77
    # a = a[K - 1::-1] + a[N:K - 1:-1]
    # print(a)
    #third way
    # i = 0
    # j = len(a)-1
    # for x in range(n):
    #     fe = a[i]
    #     for y in range(j):
    #         a[y] = a[y+1]
    #     a[j] = fe
    # print(a)

a = []
ne = int(input("enter the number of elements:\n"))
for i in range(0,ne):
	e = int(input("enter the elements you want in list:\n"))
	a.append(e)
print(a)
# arr =[1,2,3,4]
d = int(input("enter the number you wanna rotate"))
print(rotate(d,arr))


