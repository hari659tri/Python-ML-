# row=int(input())
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
    

# print(90 and 9)
# print([] or 3) #3
# print(""or 90) #90
# print(90 or 9) #90
# print('hari'or 0) #'hari'
# row=int(input())

# for i in range(1,row+1):
#     for j in range(1,row+2-i):
#         print("*",end="")
#     print()

# row=int(input())
# col=int(input())
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if row+1-i<=j and j<row+i:
#          print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
    
    
#check entered number fibonaci number or not
# import math 
# # print(int(math.sqrt(4)))
# def perfectsquare(num):
#     square_root=int(math.sqrt(num))
#     return square_root**2==num
# def chechkfib(n):
#     if perfectsquare(5*n**2+4)or perfectsquare(5*n**2-4):
#         return True
#     return False

# if(chechkfib(3)):
#     print("yes fibonaci number")
# else:
#     print("not a fibonaci number")

row=int(input())

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
for i in range(1,row):
    for j in range(1,row+1-i):
        print("*",end=" ")
    print()
