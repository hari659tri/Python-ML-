# def isarmstrong(num):
#     str_num=str(num)
#     len_num=len(str_num)
#     sum=0
#     org=num
#     while num>0:
#         rem=num%10
#         sum=sum+rem**len_num
#         num=num//10
    
#     return org==sum
 
# num=int(input("enter a number "))
# if isarmstrong(num):
#     print("yes number is armstrong number ")
# else:
#     print("not a armastrong number")


#plandrome check program

# def isplandrome(num:int)->bool:
#     org=num
#     rev=0
#     while num>0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     print(rev)
#     return org==rev

# if isplandrome(int(input())):
#     print("yes plandrome")
# else:
#     print("not a plandrome")

#fibonacci series upto n terms
# def fibonaci(n):
#     series=[]
#     a,b=0,1
#     while len(series)<n:
#         series.append(a)
#         a,b=b,a+b
        
#     return series

# print(fibonaci(10))

#factorial of a number 
# def fact(n):
#     fact=1
#     for i in range(2,n+1):
#         fact=fact*i
#     return fact

# print(fact(10))
#check given number is prime or not 

# def prime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     else:
#        return True

# if prime(int(input())):
#     print("yes prime number")
# else:
#     print("not a prime number")
    
    
#genrate a prime number in the range (a,b) where a and b not included 
lower=int(input())
upper=int(input())
for num in range(lower+1,upper):
    if(num>1):
        for i in range(2,num):
          if(num%i)==0:
              break
        else:
            print(f"prime number in {[lower,upper]} range is {num}",end=" ")
        
    else:
        print(f"{num} not a prime number")
              
        
        
        