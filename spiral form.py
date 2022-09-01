m = int(input("enter the number of rows: \n"))
n = int(input("enter the number of columns: \n"))
a = []
for i in range(m):
    b = []
    for j in range(n):
        j = input("enter element [" + str(i) + "][" + str(j) + "]")
        b.append(j)
    a.append(b)
print("Matrix is....")
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
# SPIRAL FUNCTION
row = 0
col = 0
while row < m and col < n:
    for i in range(col,n):
        print(a[row][i],end = " ")
    row = row+1
    for i in range(row,m):
        print(a[i][n-1],end=" ")
    n =n-1
    if row < m :
        for i in range(n-1,(col-1),-1):
            print(a[m-1][i],end=" ")
        m=m-1
    if col < n:
        for i in range(m-1,(row-1),-1):
            print(a[i][col],end=" ")
        col=col+1


