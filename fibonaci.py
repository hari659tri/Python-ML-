#print sequence of fibonaci serires of n terms

def fibonaciseries(n):
   """
    Generate a Fibonacci series up to n terms.
    """
   series=[] #here we creared an a empty list of size zero 
   a,b=0,1
   while len(series)<n:
       series.append(a)
       a,b=b,a+b  # updarting value of a in each round by b and b also update
       
   return   series

n=int(input())
if(n<0):
    print("please enter the potive integer term or number of sequence not be empty")
else:
    series=fibonaciseries(n)
    print(series)
    print(type(series))
