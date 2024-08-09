def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("plese enter a input for\n sum press 1\n for subtract press 2\n for multiply press 3\n for divide press 4\n")

select=int(input())
num1=int(input("please enter number1 "))
num2=int(input("please enter number2 "))

if select==1:
    print(f"{num1}+{num2} is {sum(num1,num2)}")
elif select==2:
    print(f"{num1}-{num2} is {subtract(num1,num2)}")
elif select==3:
    print(f"{num1}*{num2} is {multiply(num1,num2)}")
elif select==4:
     print(f"{num1}/{num2} is {divide(num1,num2)}")
else:
    print("invalid input")