row=int(input())
col=int(input())
for i in range(1,row+1):
    for j in range(1,col+1):
        if(j<=i):
            print("*",end=" ")     
        else:
            print(" ",end=" ")
            
    print()
   
for i in range(1,row):
    for j in range(1,col+1-i):
        print("*",end=" ")
    print()
    