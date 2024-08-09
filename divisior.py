def factor(num):
    list=[]
    if(num>=1):
         for i in range(1,num+1):
             if num%i==0:
              list.append(i)
    return list
        



print(factor(int(input("enter a number greater then equal to 1"))))