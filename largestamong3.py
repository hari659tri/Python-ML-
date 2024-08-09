def maxofthree(a,b,c):
     if a>b and a>c:
           return a
     elif b>a and b>c:
           return b
     else:
           return c
           

x=int(input())
y=int(input())
z=int(input())
print(type(x))
print(maxofthree(x,y,z))

def leapyear(year):
      if year%400==0:
            print("year is a leap year")
      elif year%100==00:
            print("year is not a leap year")
      elif year%4==0:
            print("year is a leap year")
      else:
            print("year is not a leap year")

year=int(input())
leapyear(year)
      
# calculator
num1=int(input())
num2=int(input())
operator=input("enter a opeartor +,-,*,/,//: ")
if operator=='+':
      print(f'{num1}+{num2} is {num1+num2}')
elif operator=='-':
      print(f'{num1}-{num2} is {num1-num2}')
elif operator=='*':
      print(f"{num1}*{num2} is {num1*num2}")
elif operator=='/':
      print(f"{num1}/{num2} is {num1/num2}")
elif operator=='//':
      print(f"{num1}//{num2} is {num1//num2}")
else:
      print(f"invalid input {operator}")
for i in range(10,3):
     print(i)