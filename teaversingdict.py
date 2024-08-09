# d={'a':1,'b':2,'c':3}
# for key in d:
#     print(key,d[key])

# for key,value in d.items():
#     print(key,value)

#using while loop
# list=list(d.items())
# index=0
# while index<len(list):
#     key,value=list[index]
#     print(key,value)
#     index+=1

#conversion of decimal number 
# def convert(num):
#     print(bin(num))
#     print(oct(num))
#     print(hex(num))
# convert(10)

def removekth(s,k):
    if(k>=len(s)):
        return s
    str=""
    for i in range(len(s)):
        if(i!=k):
            str=str+s[i]
    
    return str

print(removekth("python",2))
print(removekth("python",5))
print(removekth("mango",5))
