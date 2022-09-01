A = []
N,K = int(input("enter the array size")),int(input("enter the K"))
for i in range(N):
    ele = int(input("enter the Element"))
    A.append(ele)

M = (N*K)/2
res = 0
while M>0:
    for i in range(N):
        res = res + A[i]
        # print(res)
    M-=1
print(res)