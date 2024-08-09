#count the number of digit,uppercase and lowercase char

def calculate(str:str)->dict:
    d={"upper_case":0,"lower_case":0,"digit":0}
    for s in str:
        if(s.isupper()):
            d["upper_case"]+=1
        elif s.islower():
            d["lower_case"]+=1
        elif s.isdigit():
            d["digit"]+=1
            
    return d


dic=calculate("STRINGhappy$%&Y34573y")
print(dic)

# s="STRINGhappy$%&Y34573y"
# c1=0
# c2=0
# for i in s:
#     c1+=1

# for i in range(len(s)):
#     print(s[i])
#     c2+=1

# print()

# print(c1,c2)