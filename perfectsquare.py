#check give numbder is perfect square or not 
import math
def perfectsquare(num):
     
     square_root=int(math.sqrt(num))
     return square_root**2==num
    
    

number=int(input())
if number>=0:
   is_perfect= perfectsquare(number)
   if(is_perfect):
       print(f"{number} is a perfect square")
   else:
       print(f"entered {number} not a perfect saquare")
else:
    print(f"not accept the negative {number}")
    