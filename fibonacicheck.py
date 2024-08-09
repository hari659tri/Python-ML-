#check given number is fibonaci or not
import math
def isperfect_square(num): 
    square_root=int(math.sqrt(num))
    return square_root**2==num

def isfibonaci(num):
  
    if isperfect_square(5*(num**2)+4) or isperfect_square(5*(num**2)-4):
        return True
    else:
        return False




number=int(input())

if(isfibonaci(number)):
    print(f"{number} is a fibonaci number")
else:
    print(f"{number} not a fibonacci number")
