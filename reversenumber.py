#456->654

def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10 # we prform here integer division not float division 
        
    return sum

print(reverse(65498765))

#print(567//10)