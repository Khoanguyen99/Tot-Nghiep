# # 5.1
#
# def Input():
#     L = []
#     n=int(input("n="))
#     i=0
#     while i < n:
#         a=int(input())
#         L = L + [a]
#         i=i+1
#     x=int(input("x="))
#     return  n,x,L
#
# def FirstAndLast(L):
#     newList = [L[0],L[-1]]
#     return  newList
#
# def Search(L,x):
#     if x in L:
#         return True
#     else:
#         return False
#
# n,x,L=Input()
# print(FirstAndLast(L))
# print(Search(L,x))

# # Bai5.2
# def Input():
#     L=[]
#     n=int(input("n="))
#     i=0
#     while (i<n):
#         a=int(input())
#         L.append(a)
#         i=i+1
#     return L
# def Search(L):
#     L.sort()
#     min = L[0]
#     max = L[-1]
#     return max,min
# def Output(max, min):
#     print(max, min)
#
# L=Input()
# max,min = Search(L)
# Output(max, min)

## Bai5.3
# Khong dung ham
# n=int(input("n="))
# L=[]
# i=0
# SND=0
# while (i<n):
#     a=int(input())
#     L=L+[a]
#     if (a>0):
#         SND+=1
#     i+=1
# count=0
# sum=0
# j=0
# TBC=0
# for j in L:
#     if j%2 == 0:
#         count+=1
#         sum=sum+j
# if (count==0):
#     TBC=0
# else:
#     TBC=sum/count
#
# print("SND=",SND,sep="")
# print("TBC=",round(TBC,2),sep="")

# # Dung ham
# def Input():
#     L=[]
#     n=int(input("n="))
#     i=0
#     while (i<n):
#         a=int(input())
#         L = L+[a]
#         i+=1
#     return L
#
# def countInteger(L):
#     Integer=0
#     for j in L:
#         if j>0:
#           Integer+=1
#     return Integer
#
# def Avg(L):
#     count=0
#     sum=0
#     TBC=0
#     for x in L:
#         if (x%2==0):
#             count+=1
#             sum=sum+x
#         if (count>0):
#             TBC = sum / count
#         else:
#             TBC=0
#     return TBC
#
# L=Input()
# print("SND=",countInteger(L),sep="")
# print("TBC=",Avg(L),sep="")

# # Bai5.4
# khong dung ham
# n=int(input("n="))
# A=[]
# i=0
# while (i<n):
#     a=int(input())
#     A=A+[a]
#     i=i+1
# n=len(A)
# B=[]
# for j in range(n-1,-1,-1):
#     B.append(A[j])
# print(B, sep="")

#
#  Dung ham
# def Input():
#     n=int(input("n="))
#     i=0
#     A=[]
#     while (i<n):
#         a=int(input())
#         A=A+[a]
#         i+=1
#     return A
#
# def daoNguoc(A):
#     B=[]
#     n=len(A)
#     for j in range (n-1,-1,-1):
#         B.append(A[j])
#     return B
#
# def sapxep(A):
#     B=[]
#     while True:
#         m=min(A)
#         B.append(m)
#         A.remove(m)
#         if len(A) ==0:
#             break
#     return B
#
#
# def InKQ(B):
#    print("[", end="")
#    n=len(B)
#    for i in range(0,n-1):
#        print(B[i],end=" ")
#    print(B[n-1],"]",sep="")
# A= Input()
# B=daoNguoc(A)
# InKQ(B)
# B=sapxep(A)
# InKQ(B)

# # Bai 5.5
# def Input():
#     n=int(input("n="))
#     i=0
#     A=[]
#     while (i<n):
#         a=int(input())
#         A=A+[a]
#         i+=1
#     return A
#
# def printEvenInteger(A):
#     n=len(A)
#     sum=0
#     for i in range (0,n-1,1):
#         if (i%2==1):
#             sum =sum + A[i]
#     return sum
#
# A=Input()
# print("Tong=",printEvenInteger(A),sep="")

# Bai 5.6
# def Input():
#     i=0
#     A=[]
#     while(i<10):
#         n=int(input())
#         A=A+[n]
#         i+=1
#     return A
#
# def Reserve(A):
#     B=[]
#     for i in range (0,10,2):
#         B.append(A[i+1])
#         B.append(A[i])
#     return B
# def Result(B):
#     for i in range (0,10,1):
#         print(B[i],end=" ")
#
# A=Input()
# B=Reserve(A)
# Result(B)

# #  Bai 5.7
# def Input():
#     L=[]
#     n=int(input("n="))
#     i=0
#     while (i<n):
#         a=int(input())
#         L.append(a)
#         i+=1
#     return L
#
# def ResultM(L):
#     M=[]
#     for i in L:
#         if i not in M:
#             M.append(i)
#     return M
#
# def InKQ(M):
#     for i in M:
#         print(i,end=" ")
#
# L=Input()
# M=ResultM(L)
# InKQ(M)

#  Bai5.9
# L3=[]
# def Input():
#     n=int(input("n="))
#     m=int(input("m="))
#     L1=[]
#     L2=[]
#     print("L1: ")
#     for i in range (0,n,1):
#         a=int(input())
#         L1.append(a)
#     print("L2: ")
#     for j in range (0,m,1):
#         b=int(input())
#         L2.append(b)
#     return L1,L2
#
# def Result(L1,L2):
#     for x in (L1+L2):
#         if x not in L3 and (L1+L2).count(x)==2:
#             L3.append(x)
#     return L3
#
# def InKQ(L3):
#     print("L3:", end="")
#     for y in L3:
#         print(y,end=" ")
# L1,L2=Input()
# Result(L1,L2)
# InKQ(L3)

#Bai5.10
# n = int(input("n="))
# matrix = []
# for i in range(0, 3):
#     matrix.append([])
#     for j in range(0, n):
#         matrix[i].append(0)
#
# k = 1
# while k <= n:
#     print("Hoc sinh ",k,": ",sep="")
#     Toan=int(input("Toan="))
#     if Toan < 0 :
#         print("Vui long kiem tra lai diem Toan ")
#         break
#     else:
#         matrix[0][k-1]=Toan
#     Ly = int(input("Ly="))
#     if Ly < 0 :
#         print("Vui long kiem tra lai diem Ly ")
#         break
#     else:
#         matrix[1][k-1]=Ly
#
#     matrix[2][k-1]=(Toan+Ly)/2
#     k=k+1
#
# print("DTB cao nhat:",max(matrix[2]))

# Bai in sao nguoc
# i=1
# while i<=9:
#     j=9
#     while j>=i:
#         print("$",end="")
#         j=j-1
#     print("\n")
#     i=i+1

