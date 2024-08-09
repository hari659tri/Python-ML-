def fib(n,list,a,b):
    if len(list)>=n:
        return
    sum=a
    list.append(sum)
    a,b=b,a+b
    return fib(n,list,a,b)





n=int(input("enter how many sequence of number dispaly in fib series"))
list=[]
fib(n,list,0,1)

for i in range(len(list)):  
    print(list[i],end=",")