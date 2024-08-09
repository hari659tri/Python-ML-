low=int(input())
upper=int(input())
print("printing the number in the given range are")
for num in range(low,upper+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)  #[53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            
    